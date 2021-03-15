from flask import Flask
app = Flask('app')

@app.route('/')
def root_home():
  return 'err:inv_syt'
@app.route('/statuspage')
def get_status()


app.run(host='0.0.0.0', port=8080)