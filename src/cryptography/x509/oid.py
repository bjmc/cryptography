# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

from cryptography import utils
from cryptography.hazmat.primitives import hashes


class ObjectIdentifier(object):
    def __init__(self, dotted_string):
        self._dotted_string = dotted_string

    def __eq__(self, other):
        if not isinstance(other, ObjectIdentifier):
            return NotImplemented

        return self.dotted_string == other.dotted_string

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "<ObjectIdentifier(oid={0}, name={1})>".format(
            self.dotted_string,
            _OID_NAMES.get(self, "Unknown OID")
        )

    def __hash__(self):
        return hash(self.dotted_string)

    dotted_string = utils.read_only_property("_dotted_string")


OID_SUBJECT_DIRECTORY_ATTRIBUTES = ObjectIdentifier("2.5.29.9")
OID_SUBJECT_KEY_IDENTIFIER = ObjectIdentifier("2.5.29.14")
OID_KEY_USAGE = ObjectIdentifier("2.5.29.15")
OID_SUBJECT_ALTERNATIVE_NAME = ObjectIdentifier("2.5.29.17")
OID_ISSUER_ALTERNATIVE_NAME = ObjectIdentifier("2.5.29.18")
OID_BASIC_CONSTRAINTS = ObjectIdentifier("2.5.29.19")
OID_CRL_REASON = ObjectIdentifier("2.5.29.21")
OID_INVALIDITY_DATE = ObjectIdentifier("2.5.29.24")
OID_CERTIFICATE_ISSUER = ObjectIdentifier("2.5.29.29")
OID_NAME_CONSTRAINTS = ObjectIdentifier("2.5.29.30")
OID_CRL_DISTRIBUTION_POINTS = ObjectIdentifier("2.5.29.31")
OID_CERTIFICATE_POLICIES = ObjectIdentifier("2.5.29.32")
OID_POLICY_MAPPINGS = ObjectIdentifier("2.5.29.33")
OID_AUTHORITY_KEY_IDENTIFIER = ObjectIdentifier("2.5.29.35")
OID_POLICY_CONSTRAINTS = ObjectIdentifier("2.5.29.36")
OID_EXTENDED_KEY_USAGE = ObjectIdentifier("2.5.29.37")
OID_FRESHEST_CRL = ObjectIdentifier("2.5.29.46")
OID_INHIBIT_ANY_POLICY = ObjectIdentifier("2.5.29.54")
OID_AUTHORITY_INFORMATION_ACCESS = ObjectIdentifier("1.3.6.1.5.5.7.1.1")
OID_SUBJECT_INFORMATION_ACCESS = ObjectIdentifier("1.3.6.1.5.5.7.1.11")
OID_OCSP_NO_CHECK = ObjectIdentifier("1.3.6.1.5.5.7.48.1.5")

OID_COMMON_NAME = ObjectIdentifier("2.5.4.3")
OID_COUNTRY_NAME = ObjectIdentifier("2.5.4.6")
OID_LOCALITY_NAME = ObjectIdentifier("2.5.4.7")
OID_STATE_OR_PROVINCE_NAME = ObjectIdentifier("2.5.4.8")
OID_ORGANIZATION_NAME = ObjectIdentifier("2.5.4.10")
OID_ORGANIZATIONAL_UNIT_NAME = ObjectIdentifier("2.5.4.11")
OID_SERIAL_NUMBER = ObjectIdentifier("2.5.4.5")
OID_SURNAME = ObjectIdentifier("2.5.4.4")
OID_GIVEN_NAME = ObjectIdentifier("2.5.4.42")
OID_TITLE = ObjectIdentifier("2.5.4.12")
OID_GENERATION_QUALIFIER = ObjectIdentifier("2.5.4.44")
OID_DN_QUALIFIER = ObjectIdentifier("2.5.4.46")
OID_PSEUDONYM = ObjectIdentifier("2.5.4.65")
OID_DOMAIN_COMPONENT = ObjectIdentifier("0.9.2342.19200300.100.1.25")
OID_EMAIL_ADDRESS = ObjectIdentifier("1.2.840.113549.1.9.1")

OID_RSA_WITH_MD5 = ObjectIdentifier("1.2.840.113549.1.1.4")
OID_RSA_WITH_SHA1 = ObjectIdentifier("1.2.840.113549.1.1.5")
OID_RSA_WITH_SHA224 = ObjectIdentifier("1.2.840.113549.1.1.14")
OID_RSA_WITH_SHA256 = ObjectIdentifier("1.2.840.113549.1.1.11")
OID_RSA_WITH_SHA384 = ObjectIdentifier("1.2.840.113549.1.1.12")
OID_RSA_WITH_SHA512 = ObjectIdentifier("1.2.840.113549.1.1.13")
OID_ECDSA_WITH_SHA1 = ObjectIdentifier("1.2.840.10045.4.1")
OID_ECDSA_WITH_SHA224 = ObjectIdentifier("1.2.840.10045.4.3.1")
OID_ECDSA_WITH_SHA256 = ObjectIdentifier("1.2.840.10045.4.3.2")
OID_ECDSA_WITH_SHA384 = ObjectIdentifier("1.2.840.10045.4.3.3")
OID_ECDSA_WITH_SHA512 = ObjectIdentifier("1.2.840.10045.4.3.4")
OID_DSA_WITH_SHA1 = ObjectIdentifier("1.2.840.10040.4.3")
OID_DSA_WITH_SHA224 = ObjectIdentifier("2.16.840.1.101.3.4.3.1")
OID_DSA_WITH_SHA256 = ObjectIdentifier("2.16.840.1.101.3.4.3.2")

_SIG_OIDS_TO_HASH = {
    OID_RSA_WITH_MD5.dotted_string: hashes.MD5(),
    OID_RSA_WITH_SHA1.dotted_string: hashes.SHA1(),
    OID_RSA_WITH_SHA224.dotted_string: hashes.SHA224(),
    OID_RSA_WITH_SHA256.dotted_string: hashes.SHA256(),
    OID_RSA_WITH_SHA384.dotted_string: hashes.SHA384(),
    OID_RSA_WITH_SHA512.dotted_string: hashes.SHA512(),
    OID_ECDSA_WITH_SHA1.dotted_string: hashes.SHA1(),
    OID_ECDSA_WITH_SHA224.dotted_string: hashes.SHA224(),
    OID_ECDSA_WITH_SHA256.dotted_string: hashes.SHA256(),
    OID_ECDSA_WITH_SHA384.dotted_string: hashes.SHA384(),
    OID_ECDSA_WITH_SHA512.dotted_string: hashes.SHA512(),
    OID_DSA_WITH_SHA1.dotted_string: hashes.SHA1(),
    OID_DSA_WITH_SHA224.dotted_string: hashes.SHA224(),
    OID_DSA_WITH_SHA256.dotted_string: hashes.SHA256()
}

OID_SERVER_AUTH = ObjectIdentifier("1.3.6.1.5.5.7.3.1")
OID_CLIENT_AUTH = ObjectIdentifier("1.3.6.1.5.5.7.3.2")
OID_CODE_SIGNING = ObjectIdentifier("1.3.6.1.5.5.7.3.3")
OID_EMAIL_PROTECTION = ObjectIdentifier("1.3.6.1.5.5.7.3.4")
OID_TIME_STAMPING = ObjectIdentifier("1.3.6.1.5.5.7.3.8")
OID_OCSP_SIGNING = ObjectIdentifier("1.3.6.1.5.5.7.3.9")

OID_CA_ISSUERS = ObjectIdentifier("1.3.6.1.5.5.7.48.2")
OID_OCSP = ObjectIdentifier("1.3.6.1.5.5.7.48.1")

OID_CPS_QUALIFIER = ObjectIdentifier("1.3.6.1.5.5.7.2.1")
OID_CPS_USER_NOTICE = ObjectIdentifier("1.3.6.1.5.5.7.2.2")
OID_ANY_POLICY = ObjectIdentifier("2.5.29.32.0")

_OID_NAMES = {
    OID_COMMON_NAME: "commonName",
    OID_COUNTRY_NAME: "countryName",
    OID_LOCALITY_NAME: "localityName",
    OID_STATE_OR_PROVINCE_NAME: "stateOrProvinceName",
    OID_ORGANIZATION_NAME: "organizationName",
    OID_ORGANIZATIONAL_UNIT_NAME: "organizationalUnitName",
    OID_SERIAL_NUMBER: "serialNumber",
    OID_SURNAME: "surname",
    OID_GIVEN_NAME: "givenName",
    OID_TITLE: "title",
    OID_GENERATION_QUALIFIER: "generationQualifier",
    OID_DN_QUALIFIER: "dnQualifier",
    OID_PSEUDONYM: "pseudonym",
    OID_DOMAIN_COMPONENT: "domainComponent",
    OID_EMAIL_ADDRESS: "emailAddress",
    OID_RSA_WITH_MD5: "md5WithRSAEncryption",
    OID_RSA_WITH_SHA1: "sha1WithRSAEncryption",
    OID_RSA_WITH_SHA224: "sha224WithRSAEncryption",
    OID_RSA_WITH_SHA256: "sha256WithRSAEncryption",
    OID_RSA_WITH_SHA384: "sha384WithRSAEncryption",
    OID_RSA_WITH_SHA512: "sha512WithRSAEncryption",
    OID_ECDSA_WITH_SHA1: "ecdsa-with-SHA1",
    OID_ECDSA_WITH_SHA224: "ecdsa-with-SHA224",
    OID_ECDSA_WITH_SHA256: "ecdsa-with-SHA256",
    OID_ECDSA_WITH_SHA384: "ecdsa-with-SHA384",
    OID_ECDSA_WITH_SHA512: "ecdsa-with-SHA512",
    OID_DSA_WITH_SHA1: "dsa-with-sha1",
    OID_DSA_WITH_SHA224: "dsa-with-sha224",
    OID_DSA_WITH_SHA256: "dsa-with-sha256",
    OID_SERVER_AUTH: "serverAuth",
    OID_CLIENT_AUTH: "clientAuth",
    OID_CODE_SIGNING: "codeSigning",
    OID_EMAIL_PROTECTION: "emailProtection",
    OID_TIME_STAMPING: "timeStamping",
    OID_OCSP_SIGNING: "OCSPSigning",
    OID_SUBJECT_DIRECTORY_ATTRIBUTES: "subjectDirectoryAttributes",
    OID_SUBJECT_KEY_IDENTIFIER: "subjectKeyIdentifier",
    OID_KEY_USAGE: "keyUsage",
    OID_SUBJECT_ALTERNATIVE_NAME: "subjectAltName",
    OID_ISSUER_ALTERNATIVE_NAME: "issuerAltName",
    OID_BASIC_CONSTRAINTS: "basicConstraints",
    OID_CRL_REASON: "cRLReason",
    OID_INVALIDITY_DATE: "invalidityDate",
    OID_CERTIFICATE_ISSUER: "certificateIssuer",
    OID_NAME_CONSTRAINTS: "nameConstraints",
    OID_CRL_DISTRIBUTION_POINTS: "cRLDistributionPoints",
    OID_CERTIFICATE_POLICIES: "certificatePolicies",
    OID_POLICY_MAPPINGS: "policyMappings",
    OID_AUTHORITY_KEY_IDENTIFIER: "authorityKeyIdentifier",
    OID_POLICY_CONSTRAINTS: "policyConstraints",
    OID_EXTENDED_KEY_USAGE: "extendedKeyUsage",
    OID_FRESHEST_CRL: "freshestCRL",
    OID_INHIBIT_ANY_POLICY: "inhibitAnyPolicy",
    OID_AUTHORITY_INFORMATION_ACCESS: "authorityInfoAccess",
    OID_SUBJECT_INFORMATION_ACCESS: "subjectInfoAccess",
    OID_OCSP_NO_CHECK: "OCSPNoCheck",
    OID_OCSP: "OCSP",
    OID_CA_ISSUERS: "caIssuers",
    OID_CPS_QUALIFIER: "id-qt-cps",
    OID_CPS_USER_NOTICE: "id-qt-unotice",
}