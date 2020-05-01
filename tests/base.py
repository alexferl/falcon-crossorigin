import unittest

from falcon_crossorigin import CrossOrigin

import falcon
import falcon.testing


class TestBase(unittest.TestCase):
    def setUp(self, cross_origin=None):
        if not cross_origin:
            cross_origin = CrossOrigin()
        self.app = falcon.API(middleware=[cross_origin])
        self.srmock = falcon.testing.StartResponseMock()

    def simulate_request(self, path, *args, **kwargs):
        env = falcon.testing.create_environ(path, *args, **kwargs)
        self.app(env, self.srmock)
        self.res_headers = self.srmock.headers_dict

    def simulate_get(self, *args, **kwargs):
        kwargs["method"] = "GET"
        return self.simulate_request(*args, **kwargs)

    def simulate_post(self, *args, **kwargs):
        kwargs["method"] = "POST"
        return self.simulate_request(*args, **kwargs)

    def simulate_put(self, *args, **kwargs):
        kwargs["method"] = "PUT"
        return self.simulate_request(*args, **kwargs)

    def simulate_delete(self, *args, **kwargs):
        kwargs["method"] = "DELETE"
        return self.simulate_request(*args, **kwargs)

    def simulate_patch(self, *args, **kwargs):
        kwargs["method"] = "PATCH"
        return self.simulate_request(*args, **kwargs)

    def simulate_head(self, *args, **kwargs):
        kwargs["method"] = "HEAD"
        return self.simulate_request(*args, **kwargs)

    def simulate_options(self, *args, **kwargs):
        kwargs["method"] = "OPTIONS"
        return self.simulate_request(*args, **kwargs)
