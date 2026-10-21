import sys
"""src/ 를 합쳐 index.html (로컬·zip용) 과 pub/bc-home.html (게시용) 을 만든다."""
import os,glob
S='src/'
base=open(S+'base.html').read()
MODULES=['people','about','product','partner','ir','esg','contact']
css=''.join(open(S+m+'.css').read()+'\n' for m in MODULES if os.path.exists(S+m+'.css'))
parts=[open(S+'core.js').read(),open(S+'data.js').read()]+[open(S+m+'.js').read() for m in MODULES if os.path.exists(S+m+'.js')]
js='\n</script>\n<script>\n'.join(parts)
out=base.replace('</style>',css+'\n</style>',1)
i=out.index('<script>\n(function(){')
out=out[:i]+'<script>\n'+js+'\n</script>\n'+out[i:]
j=out.rindex('</script>')
out=out[:j]+'\nBC.start();\n'+out[j:]
if len(sys.argv)>1:
    open(sys.argv[1],'w').write(out); sys.exit()
open('index.html','w').write(out)
os.makedirs('pub',exist_ok=True)
open('pub/bc-home.html','w').write('\n'.join(l for l in out.split('\n') if '<!--PRETENDARD-->' not in l))
print('built', len(out)//1024,'KB')
