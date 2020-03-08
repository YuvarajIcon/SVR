import re
import urllib.request

class svr:
    def python():
        page=urllib.request.urlopen('https://www.python.org/doc/versions/')
        l=page.read()
        c=l.decode('ASCII')
        file=open("x.txt","w")
        file.write(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
            
            if('<li><a class="reference external" href="http://docs.python.org/release' in line):
               s=open("x.txt","w")
               s.write(line)
               result=re.search('Python (.*)</a>',line)
               b = result.group(1)
               return(b)
        
               
    def ruby():
        page=urllib.request.urlopen('https://www.ruby-lang.org/en/downloads/')
        c=page.read()           
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        s=open("x.txt","r")
        result=re.search('The current stable version is (.*)Please be sure',q)
        b = result.group(1)
        return(b[:-3])
        
    def android_studio():
        page=urllib.request.urlopen('https://developer.android.com/studio/releases/')
        c=page.read()
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           s=open("x.txt","w")
           result=re.search('<p><b>(.*)</b></p>',line)
           b = result.group(1)
           a=b.split()
           return(a[0])
        
    def mongoserver():
        page=urllib.request.urlopen('https://docs.mongodb.com/manual/release-notes/')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('<meta name="release" content="(.*)"/>',line)
           b = result.group(1)
           a=b.split()
           return(a[0][:5])
        
    def blender():
        page=urllib.request.urlopen('https://www.blender.org/download/')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('www.blender.org/download/Blender(.*)/blender-',line)
           b = result.group(1)
           a=b.split()
           return(a[0][:4])
    
    def unity():
        page=urllib.request.urlopen('https://unity3d.com/unity/qa/lts-releases')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('<p>We are happy to announce Unity (.*). The rel',line)
           b = result.group(1)
           a=b.split()
           return(a[0][:-1])
    
    def visual_studio():
        page=urllib.request.urlopen('https://visualstudio.microsoft.com/downloads/')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('<p class="notes-top">Version (.*)</p>',line)
           b = result.group(1)
           a=b.split()
           return(a[0][:4])
        
    def vscode():
        page=urllib.request.urlopen('https://code.visualstudio.com/download')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('<span itemprop="softwareVersion">(.*)</span></a> is now ',line)
           b = result.group(1)
           a=b.split()
           return(a[0])
        
    def postgresql():
        page=urllib.request.urlopen('https://www.postgresql.org/')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('>PostgreSQL (.*) Released!</a>',line)
           b = result.group(1)
           a=b.split()
           a.remove('and')
           a=[i.replace(',','')for i in a]
           return(a[:6])
        
    def mariadb():
        page=urllib.request.urlopen('https://mariadb.org/download/')
        c=page.read() 
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
           result=re.search('<a href="https://downloads.mariadb.org/mariadb/(.*)/">',line)
           b = result.group(1)
           a=b.split()
           a=str(a[3:8])
           a=re.findall("\d+\.\d+\.\d+",a)
           a=list(dict.fromkeys(a))
           return(a)
           
               


            


