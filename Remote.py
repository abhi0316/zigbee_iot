import urllib2, base64
import json
import urllib
import datetime
import threading

url ="endpoint here"
username="username"
password="password"



def send_report(CCId, SensorID, OccState):
    #parameterString = json.dumps({
     #   "ccid": CCId,
     #   "ts": int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds()),
     #   "d": [{ "sid": SensorID, "eid": 0, "occ": OccState }]
	
      #  })
    #print parameterString
    parameterString1 =urllib.urlencode({

        "d": [
                {"occ": OccState,
                "eid": 0,
                "sid":SensorID
                }
                ],
        "ccid": CCId,
        "ts": int((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds())

        })

    #queryString = urllib.urlencode({REPORT_PARAM_NAME: parameterString})
    #if REPORT_HTTPS:
     #   urlString = "https://"
    #else:
     #   urlString = "http://"
    #urlString += REPORT_DOMAIN+"/"+REPORT_ENDPOINT+"?"+queryString
    #print urlString
    #reader = urllib.urlopen(urlString)
    #responseString = reader.read()
    request = urllib2.Request(url,data=parameterString1)

    base64string = base64.encodestring('%s:%s' % (username,password)).replace('\n','')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    print(result.read())
    #print responseString
    #if responseString == "\nSuccess!":
	#return True
    #else:
     #   return False

def threaded_send_report(CCId, SensorID, OccState):
    thread = threading.Thread(target=send_report, args = (CCId, SensorID, OccState))
    thread.daemon = True
    thread.start()


