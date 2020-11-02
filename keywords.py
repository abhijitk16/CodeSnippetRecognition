# javakeywords = [line.rstrip() for line in open('JavaKeywords.txt')]
# pythonkeywords = [line.rstrip() for line in open('Python.txt')]
# featureset = list(set(pythonkeywords+javakeywords))
featureset = ['import', 'protected', 'private', 'strictfp', 'static', 'abstract', 'else', 'def', 'not', ':', 'from', 'in', 'elif', 'interface', 'throw', 'del', 'for', 'public', 'super', 'try', 'async', '#', 'false', 'new', 
'with', 'case', 'None', 'False', 'enum', 'throws', 'while', 'volatile', 'break', 'global', 'extends', 'finally', 'transient', 'except', 'return', 'and', 'or', 'goto', 'continue', 'instanceof', 'catch', 'final', 'pass', 'boolean', 'short', 'double', "'''", 'byte', '{', 'implements', 'class', 'as', 'nonlocal', 'char', 'switch', 'int', 'package', 'True', 'raise', 'synchronized', 'float', 'long', 'native', 'this', 'do', 
'await', 'is', 'lambda', 'true', 'null', 'assert', 'const', '}', 'yield', 'default', 'void', 'if','package','java','lang','os','System','join','split','len','lengths','sort']
# print(featureset)
python = [0]*len(featureset)
java = [0]*len(featureset)

with open("PythonTest.txt","r") as words:
    alllines = words.readlines()
    for i in alllines:
        j = i.split()
        for j in i.split():
            if(j in featureset):
                python[featureset.index(j)] =  python[featureset.index(j)]+1
print(python)

# with open("JavaTest.txt","r") as words:
#     alllines = words.readlines()
#     for i in alllines:
#         j = i.split()
#         for j in i.split():
#             if(j in featureset):
#                 java[featureset.index(j)] =  java[featureset.index(j)]+1
# print(java)

