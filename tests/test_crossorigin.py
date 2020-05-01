from falcon_crossorigin import (
    CrossOrigin,
    HEADER_ACCESS_CONTROL_ALLOW_ORIGIN,
    HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS,
    HEADER_ACCESS_CONTROL_ALLOW_METHODS,
    HEADER_ACCESS_CONTROL_MAX_AGE,
    HEADER_ORIGIN,
)

from . import base


class TestCrossOrigin(base.TestBase):
    def setUp(self, cross_origin=None):
        super(TestCrossOrigin, self).setUp(cross_origin)
        self.entry_path = "/"

    def tearDown(self):
        super(TestCrossOrigin, self).tearDown()

    def override_settings(self, **kwargs):
        self.setUp(CrossOrigin(**kwargs))

    def test_wildcard_origin(self):
        self.simulate_get(self.entry_path)
        self.assertEqual("*", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN])

    def test_allow_origin(self):
        self.override_settings(allow_origins="localhost")

        headers = {HEADER_ORIGIN: "localhost"}
        self.simulate_get(self.entry_path, headers=headers)
        self.assertEqual(
            "localhost", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN]
        )

    def test_preflight(self):
        self.override_settings(
            allow_origins="localhost", allow_credentials=True, max_age=3600
        )

        headers = {HEADER_ORIGIN: "localhost", "Content-Type": "application/json"}
        self.simulate_options(self.entry_path, headers=headers)

        self.assertEqual(
            "localhost", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN]
        )
        self.assertEqual(
            "true", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS]
        )
        self.assertNotEqual("", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_METHODS])
        self.assertEqual("3600", self.res_headers[HEADER_ACCESS_CONTROL_MAX_AGE])

    def test_preflight_wildcard_origin(self):
        self.override_settings(
            allow_origins="localhost", allow_credentials=True, max_age=3600
        )

        headers = {HEADER_ORIGIN: "localhost", "Content-Type": "application/json"}
        self.simulate_options(self.entry_path, headers=headers)

        self.assertEqual(
            "localhost", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN]
        )
        self.assertEqual(
            "true", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_CREDENTIALS]
        )
        self.assertNotEqual("", self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_METHODS])
        self.assertEqual("3600", self.res_headers[HEADER_ACCESS_CONTROL_MAX_AGE])

    def test_preflight_wildcard_origin_sub_domain(self):
        self.override_settings(allow_origins="https://*.example.com")

        headers = {
            HEADER_ORIGIN: "https://aaa.example.com",
        }
        self.simulate_options(self.entry_path, headers=headers)

        self.assertEqual(
            "https://aaa.example.com",
            self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN],
        )

        headers = {
            HEADER_ORIGIN: "https://bbb.example.com",
        }
        self.simulate_options(self.entry_path, headers=headers)

        self.assertEqual(
            "https://bbb.example.com",
            self.res_headers[HEADER_ACCESS_CONTROL_ALLOW_ORIGIN],
        )
