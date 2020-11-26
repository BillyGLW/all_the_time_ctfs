from flask import Flask, Response, session, render_template
import functools, random, string, os, re
import code
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw')

def calc(recipe):
    global garage
    print("CALC!!")
    builtins, garage = {'__builtins__': None}, {}
    try: 
        print("recipe", recipe)
        exec(recipe, builtins, garage)
    except Exception as err: 
        print("an error", err)

def GFW(func): # Great Firewall of the observable universe and it's infinite timelines
    @functools.wraps(func)
    def federation(*args, **kwargs):
        

        ingredient = session.get('ingredient', None)
        measurements = session.get('measurements', None)

        recipe = '%s = %s' % (ingredient, measurements)
        print("CHECKEDdd", recipe)
        if ingredient and measurements and len(recipe) >= 20:
            regex = re.compile('|'.join(map(re.escape, ['[', '(', '_', '.'])))
            matches = regex.findall(recipe)
            print("CHECKED")
            
            if matches: 
                print('Morty you dumbass: ' + ', '.join(set(matches)))
                return render_template('index.html', blacklisted='Morty you dumbass: ' + ', '.join(set(matches)))
            
            if len(recipe) > 300: 
                print("Za DUZE!")
                return func(*args, **kwargs) # ionic defibulizer can't handle more bytes than that
            print("rec", recipe)
            calc(recipe)
            return func(*args, **kwargs) # rick deterrent

        ingredient = session['ingredient'] = ''.join(random.choice(string.lowercase) for _ in xrange(10))
        measurements = session['measurements'] = ''.join(map(str, [random.randint(1, 69), random.choice(['+', '-', '*']), random.randint(1,69)]))

        print("[!] Checked!, Calc going to be exec...")
        calc('%s = %s' % (ingredient, measurements))
        return render_template('index.html', calculations=garage[ingredient])
    return federation

@app.route('/')
@GFW
def index():
    print("secret",app.config['SECRET_KEY'] )
    return render_template('index.html', secret=app.config['SECRET_KEY'], test="hej")
 
@app.route('/debug')
def debug():
    return Response(open(__file__).read(), mimetype='text/plain')

if __name__ == '__main__':
    app.run('0.0.0.0', port=1337)