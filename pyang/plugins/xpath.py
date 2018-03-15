"""Plugin for obtaining SysDB paths from Yang module"""

## Xpath 2.2

import optparse
import sys

from pyang import plugin

def pyang_plugin_init():
    plugin.register_plugin(XpathPlugin())

class XpathPlugin(plugin.PyangPlugin):
    def add_opts(self, optparser):
        optlist = [
            optparse.make_option("--xpath-indent",
                                 dest="xpath_indent",
                                 help="Ouput indentation"),
            ]
        g = optparser.add_option_group("xpath output specific options")
        g.add_options(optlist)        
    def add_output_format(self, fmts):
        self.multiple_modules = True
        fmts['xpath'] = self

    def emit(self, ctx, modules, fd):
        emit_xpath(ctx, modules, fd)
        
def emit_xpath(ctx, modules, fd):
    global indentNum
    indentNum = 3
    if ctx.opts.xpath_indent is not None:
        indentNum = int(ctx.opts.xpath_indent)
    for module in modules:
        makeTree(module,fd)
        
def makeTree(module,fd):
    elems = []
    groupings = []
    root = None
    bindPoint = None
    
    #Find root.
    for moduleSubstmt in module.substmts:
        for substmtSub in moduleSubstmt.substmts:
            if str(substmtSub.keyword[1]) == 'myVer-cfg-pathname':
                root = moduleSubstmt
                bindPoint = substmtSub.arg
                break
                
    #Root not found                
    if root == None:
        return

    #Find elems.
    findStatementsWithPath(module,elems)
            
    #Find all goupings.
    findGroupings(module,groupings)
    
    #Print root
    #print(str(root.arg) + ' bind point=\"' + bindPoint + '\"')
    fd.write(str(root.arg) + ' bind point=\"' + bindPoint + '\"\n')
    
    #Print path down from root
    childNum = 0
    for substmt in root.substmts:
        if substmt.keyword == 'uses':
            for grouping in groupings:
                if grouping.arg == substmt.arg:
                    childNum += len(grouping.substmts)
        if substmt in elems:
            childNum += 1
    
    #            
    for rootSubstmt in root.substmts:
        # if substatement is uses
        if rootSubstmt.keyword == 'uses':
            for grouping in groupings:
                if grouping.arg == rootSubstmt.arg:
                    for groupSubstmt in grouping.substmts:
                        if childNum > 1:
                            printPath(rootSubstmt,elems,groupings,"",2,indentNum*2*' ' +  '|' + (indentNum-1)*' ',fd) #zasah
                        else:
                            printPath(rootSubstmt,elems,groupings,"",2,indentNum*2*' ' +  indentNum*' ',fd) #zasah
                        childNum -= 1
            
        # if substatement has myVer-sch-pathname
        if rootSubstmt in elems:
            if childNum > 1:
                printPath(rootSubstmt,elems,groupings,"",2,(indentNum*2+1)*' ' +  '|' + (indentNum-1)*' ',fd) #zasah
            else:
                printPath(rootSubstmt,elems,groupings,"",2,(indentNum*2+1)*' ' +  indentNum*' ',fd) #zasah
            childNum -= 1
    
def findStatementsWithPath(statement,elems):
    for substmt in statement.substmts:
        findStatementsWithPath(substmt,elems)
        if str(substmt.keyword[1]) == 'myVer-sch-pathname': 
            elems.append(statement)
    return
    
    
def findGroupings(statement,groupings):
    for substmt in statement.substmts:
        findGroupings(substmt,groupings)
    if str(statement.keyword) == 'grouping':
            groupings.append(statement)
    return        
    
def printPath(root,elems,groupings,basePath,level,indent,fd):
    relativePath = ""
    childNum = 0
    
    for substmt in root.substmts:
        if substmt.keyword == 'uses':
            for grouping in groupings:
                if grouping.arg == substmt.arg:
                    childNum += len(grouping.substmts)
        if substmt in elems:
            childNum += 1
    
    for substmt in root.substmts:
        if str(substmt.keyword[1]) == 'myVer-sch-pathname':
            relativePath = substmt.arg
            break
    
    #print(indent[:level*indentNum+1] + "+-" + str(root.arg) + ' path=\"' + basePath + relativePath + '\"')
    fd.write(indent[:level*indentNum+1] + "+-" + str(root.arg) + ' path=\"' + basePath + relativePath + '\"\n')
    for substmt in root.substmts:
        if substmt.keyword == 'uses':
            for grouping in groupings:
                if grouping.arg == substmt.arg:
                    for groupSubstmt in grouping.substmts:
                            if childNum > 1:
                                printPath(groupSubstmt,elems,groupings,basePath + relativePath,level+1,indent +  '|' + (indentNum-1)*' ',fd) #zasah
                            else:
                                printPath(groupSubstmt,elems,groupings,basePath + relativePath,level+1,indent +  indentNum*' ',fd) #zasah
                            childNum -= 1
            
        if substmt in elems:
            if childNum > 1:
                printPath(substmt,elems,groupings,basePath + relativePath,level+1,indent +  '|' + (indentNum-1)*' ',fd)#zasah
            else:
                printPath(substmt,elems,groupings,basePath + relativePath,level+1,indent +  indentNum*' ',fd)#zasah
            childNum -= 1
