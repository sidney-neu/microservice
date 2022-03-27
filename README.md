microservice

python 3.7.3

environmental dependencies:
	requirements.txt

run:
python manage.py runserver

in another terminal run:

curl -X POST --header "Content-Type: application/json" -d '{"id":"111"}'  http://localhost:5000//example/hello_world

you will see:
{"msg":"hello world"}
