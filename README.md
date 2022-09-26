# Macaddress IO Client
A client for the macaddress.io api which can obtain details about a provided Mac address. 

## Build the docker container
To build the container run:

```
docker build . -t macaddress_client
```

## Authorisation
In order to obtain the information from the api you will need to provide an api token through an environment variable `API_TOKEN`.

I have chosen to use the header auth mechanism as this is closer to the html and tcp specs of auth in the transport layer. 
You should aim to store your api token in some kind of secrets store. As one step further, we could make it secure between the app and 
execution (some kind of CI) with some encryption but this might be overkill for this kind of service. 


## Running natively
This token can be provided as an environment variable when running the python script locally e.g.

```
export API_TOKEN=<TOKEN>
```

## Running in Docker
When running the docker image, use the -e argument to set the api token such as:

```
docker run -e API_TOKEN=<TOKEN> macaddress_client <mac_address>
```