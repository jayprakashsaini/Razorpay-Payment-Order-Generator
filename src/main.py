import razorpay
import json
razorPayId = "rzp_test_SFArDx9biTbx53"
razorPaySecret = "tROhlCkm9y2tvTORUyxrbf25"
client = razorpay.Client(auth=(razorPayId, razorPaySecret))

def main(context):
  context.log("Hello from appwrite")
  params = json.loads(context.req.body)
  amount = float(params["amount"])*100
  DATA = {
      "amount": amount,
      "currency": "INR",
      "receipt": "receipt#1",
      "notes": {
          "key1": "value3",
          "key2": "value2"
      }
  }
  response = client.order.create(data=DATA)
  context.log(f"response is {response}")
  return context.res.json(response)
