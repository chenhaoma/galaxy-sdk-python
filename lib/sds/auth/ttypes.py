# encoding: utf-8
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import sds.errors.ttypes
import sds.common.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class UserType(object):
  """
  小米存储系统认证信息类型
  """
  DEV_XIAOMI_SSO = 1
  DEV_XIAOMI = 2
  APP_SECRET = 10
  APP_ACCESS_TOKEN = 11
  APP_XIAOMI_SSO = 12
  APP_ANONYMOUS = 13

  _VALUES_TO_NAMES = {
    1: "DEV_XIAOMI_SSO",
    2: "DEV_XIAOMI",
    10: "APP_SECRET",
    11: "APP_ACCESS_TOKEN",
    12: "APP_XIAOMI_SSO",
    13: "APP_ANONYMOUS",
  }

  _NAMES_TO_VALUES = {
    "DEV_XIAOMI_SSO": 1,
    "DEV_XIAOMI": 2,
    "APP_SECRET": 10,
    "APP_ACCESS_TOKEN": 11,
    "APP_XIAOMI_SSO": 12,
    "APP_ANONYMOUS": 13,
  }

class MacAlgorithm(object):
  """
  签名使用的HMMAC算法
  """
  HmacMD5 = 1
  HmacSHA1 = 2
  HmacSHA256 = 3

  _VALUES_TO_NAMES = {
    1: "HmacMD5",
    2: "HmacSHA1",
    3: "HmacSHA256",
  }

  _NAMES_TO_VALUES = {
    "HmacMD5": 1,
    "HmacSHA1": 2,
    "HmacSHA256": 3,
  }

class AppUserAuthProvider(object):
  """
  第三方身份认证提供方，用于认证应用用户(非开发者)。
  目前提供小米SSO和几种常见OAuth系统
  """
  XIAOMI_SSO = 1
  XIAOMI_OAUTH = 2
  QQ_OAUTH = 3
  SINA_OAUTH = 4
  RENREN_OAUTH = 5

  _VALUES_TO_NAMES = {
    1: "XIAOMI_SSO",
    2: "XIAOMI_OAUTH",
    3: "QQ_OAUTH",
    4: "SINA_OAUTH",
    5: "RENREN_OAUTH",
  }

  _NAMES_TO_VALUES = {
    "XIAOMI_SSO": 1,
    "XIAOMI_OAUTH": 2,
    "QQ_OAUTH": 3,
    "SINA_OAUTH": 4,
    "RENREN_OAUTH": 5,
  }


class Credential(object):
  """
  小米存储系统认证信息

  Attributes:
   - type: 用户登录类型
   - secretKeyId: 用于服务端查询SecretKey的键值:
  1) userId: 对应User Secret
  2) appId: 对应App Secret，匿名登录也需设置
  3) storageAccessTokenId: 对应Storage Access Token
   - secretKey: Secret Key
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'secretKeyId', None, None, ), # 2
    (3, TType.STRING, 'secretKey', None, None, ), # 3
  )

  def __init__(self, type=None, secretKeyId=None, secretKey=None,):
    self.type = type
    self.secretKeyId = secretKeyId
    self.secretKey = secretKey

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.secretKeyId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.secretKey = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Credential')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.secretKeyId is not None:
      oprot.writeFieldBegin('secretKeyId', TType.STRING, 2)
      oprot.writeString(self.secretKeyId)
      oprot.writeFieldEnd()
    if self.secretKey is not None:
      oprot.writeFieldBegin('secretKey', TType.STRING, 3)
      oprot.writeString(self.secretKey)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.secretKeyId)
    value = (value * 31) ^ hash(self.secretKey)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class HttpAuthorizationHeader(object):
  """
  Authorization头包含的内容

  Attributes:
   - version
   - userType
   - secretKeyId
   - secretKey: 直接使用sercetKey，此项被设置时，signature将被忽略，
  非安全传输应使用签名
   - signature: 如secretKey未设置，则认为使用签名，此时必须设置，
  被签名的正文格式：header1[\nheader2[\nheader3[...]]]，
  如使用默认SUGGESTED_SIGNATURE_HEADERS时为：$host\n$timestamp\n$md5
   - algorithm: 签名HMAC算法，客户端可定制，
  使用签名时必须设置
   - signedHeaders: 包含所有签名涉及到的部分，建议使用SUGGESTED_SIGNATURE_HEADERS，
  服务端未强制必须使用所列headers，定制的client自己负责签名的安全强度，
  使用签名时必须设置
   - supportAccountKey
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'version', None, "SDS-V1", ), # 1
    (2, TType.I32, 'userType', None,     13, ), # 2
    (3, TType.STRING, 'secretKeyId', None, None, ), # 3
    (4, TType.STRING, 'secretKey', None, None, ), # 4
    (5, TType.STRING, 'signature', None, None, ), # 5
    (6, TType.I32, 'algorithm', None, None, ), # 6
    (7, TType.LIST, 'signedHeaders', (TType.STRING,None), [
    ], ), # 7
    (8, TType.BOOL, 'supportAccountKey', None, False, ), # 8
  )

  def __init__(self, version=thrift_spec[1][4], userType=thrift_spec[2][4], secretKeyId=None, secretKey=None, signature=None, algorithm=None, signedHeaders=thrift_spec[7][4], supportAccountKey=thrift_spec[8][4],):
    self.version = version
    self.userType = userType
    self.secretKeyId = secretKeyId
    self.secretKey = secretKey
    self.signature = signature
    self.algorithm = algorithm
    if signedHeaders is self.thrift_spec[7][4]:
      signedHeaders = [
    ]
    self.signedHeaders = signedHeaders
    self.supportAccountKey = supportAccountKey

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.version = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.userType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.secretKeyId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.secretKey = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.signature = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.algorithm = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.signedHeaders = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.signedHeaders.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.supportAccountKey = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('HttpAuthorizationHeader')
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 1)
      oprot.writeString(self.version)
      oprot.writeFieldEnd()
    if self.userType is not None:
      oprot.writeFieldBegin('userType', TType.I32, 2)
      oprot.writeI32(self.userType)
      oprot.writeFieldEnd()
    if self.secretKeyId is not None:
      oprot.writeFieldBegin('secretKeyId', TType.STRING, 3)
      oprot.writeString(self.secretKeyId)
      oprot.writeFieldEnd()
    if self.secretKey is not None:
      oprot.writeFieldBegin('secretKey', TType.STRING, 4)
      oprot.writeString(self.secretKey)
      oprot.writeFieldEnd()
    if self.signature is not None:
      oprot.writeFieldBegin('signature', TType.STRING, 5)
      oprot.writeString(self.signature)
      oprot.writeFieldEnd()
    if self.algorithm is not None:
      oprot.writeFieldBegin('algorithm', TType.I32, 6)
      oprot.writeI32(self.algorithm)
      oprot.writeFieldEnd()
    if self.signedHeaders is not None:
      oprot.writeFieldBegin('signedHeaders', TType.LIST, 7)
      oprot.writeListBegin(TType.STRING, len(self.signedHeaders))
      for iter6 in self.signedHeaders:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.supportAccountKey is not None:
      oprot.writeFieldBegin('supportAccountKey', TType.BOOL, 8)
      oprot.writeBool(self.supportAccountKey)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.version)
    value = (value * 31) ^ hash(self.userType)
    value = (value * 31) ^ hash(self.secretKeyId)
    value = (value * 31) ^ hash(self.secretKey)
    value = (value * 31) ^ hash(self.signature)
    value = (value * 31) ^ hash(self.algorithm)
    value = (value * 31) ^ hash(self.signedHeaders)
    value = (value * 31) ^ hash(self.supportAccountKey)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
