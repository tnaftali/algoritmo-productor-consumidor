from flask import Flask, request
from buffer2 import Buffer
from logger import Logger

app = Flask(__name__)

max_buffer = 50

buffer = Buffer(max_buffer)

@app.route('/produce', methods=['POST'])
def produce():
    resource = buffer.add_resource()
    return "Resource %s added to the buffer" % resource

@app.route('/consume', methods=['GET'])
def consume():
    resource = buffer.remove_resource()
    return "Resource %s consumed from the buffer" % resource

@app.route('/length', methods=['GET'])
def buffer_length():
    print(len(buffer.queue))
    return str(len(buffer.queue))

if __name__ == '__main__':
    app.run(debug=True)