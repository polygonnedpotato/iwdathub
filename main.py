from flask import Flask
import status as dathubstatus
import assetget as astg
import parsecommand as parse
app = Flask('app')

@app.route('/')
def root_home():
  return 'err:inv_syt'
@app.route('/statuspage')
def get_status():
  return 'err:not_implement'
@app.route('/getasset/<string>')
def returnasset(string):
  return 'err:not_implement'
app.run(host='0.0.0.0', port=8080)