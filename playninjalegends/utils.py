from typing import Any, List
import requests
from pyamf import remoting, AMF0


class ResponseError(Exception):
    pass


class AMFClient:
    baseURL: str
    client: requests.Session

    def __init__(self, baseURL: str) -> None:
        self.baseURL = baseURL
        self.client = requests.Session()
        self.client.headers = {
            'Content-Type': 'application/x-amf',
            'Referer': 'app:/NinjaLegends.swf',
            'Host': 'playninjalegends.com',
            'User-Agent': '',
        }

    def sendEnvelope(self, envelope: remoting.Envelope) -> remoting.Envelope:
        data = remoting.encode(envelope)
        resp = self.client.post(self.baseURL, data=data.getvalue())
        resp_msg = remoting.decode(resp.content)
        if resp_msg.bodies[0][1].status != 0:
            raise ResponseError("Response status is not 0")
        return resp_msg

    def createEnvelope(self, target: str, body: List[Any]) -> remoting.Envelope:
        req = remoting.Request(target=target, body=[body])
        ev = remoting.Envelope(AMF0)
        ev["/1"] = req
        return ev
