import unicodedata
import codecs
import re
import PyPDF2

def get_size(inp_name):
    
    pdfFileObj=open(inp_name,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    f=""
    for x in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(x)
        target=pageObj.extractText()
        f+=target
    size_pattern=re.compile(r'[\-\d.]*\s*\([\s\d\-\n,.]*,.*?\)')
    s=re.findall(size_pattern,f)
    print(s)
    size_prompt=str(input("Enter size from the following sizes {}:".format(s[0])))
    size_list=s[0].replace("(",",").replace(" ","").split(",")
    size_to_get=size_list.index(size_prompt)-1
    target_pattern_refactor=re.compile(r'{}{}{}'.format("[\-\d.]*\s*\(","[\s\d\-\n.]*,"*size_to_get,"(.*?)[,\)]"))
    target_pattern=re.compile(r'{}{}{}'.format("[0-9.]*\s*\(","[\s0-9.]*,"*size_to_get,"\s(.*?),"))
    #target_pattern_for_42=re.compile(r'[0-9.]*\s*\([\s0-9.]*,[\s0-9.]*,\s(.*?),')

    t=re.findall(target_pattern_refactor,f)
    
    n=f
    
    for i in range(len(s)):
        n=n.replace(s[i],t[i])
    final=n.split("\\r\\n")
    op_file=open("TestB/{}_Size{}.txt".format(inp_name[inp_name.index("/")+1:inp_name.index(".")],size_prompt),"w")
    for x in final:
        op_file.write(x)
        op_file.write("\n")

    op_file.close()
    pdfFileObj.close()
    print("File is saved as {}_Size{}.txt".format(inp_name[inp_name.index("/")+1:inp_name.index(".")],size_prompt))

get_size("TestB/Salal_03.pdf")
