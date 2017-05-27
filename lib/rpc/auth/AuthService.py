# encoding: utf-8
#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import rpc.common.BaseService
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(rpc.common.BaseService.Iface):
  """
  授权相关接口(目前尚未开放)
  """
  def createCredential(self, xiaomiAppId, appUserAuthProvider, authToken):
    """
    通过第三方认证系统换发Storage Access Token，采用App Secret登录无需此过程

    Parameters:
     - xiaomiAppId
     - appUserAuthProvider
     - authToken
    """
    pass


class Client(rpc.common.BaseService.Client, Iface):
  """
  授权相关接口(目前尚未开放)
  """
  def __init__(self, iprot, oprot=None):
    rpc.common.BaseService.Client.__init__(self, iprot, oprot)

  def createCredential(self, xiaomiAppId, appUserAuthProvider, authToken):
    """
    通过第三方认证系统换发Storage Access Token，采用App Secret登录无需此过程

    Parameters:
     - xiaomiAppId
     - appUserAuthProvider
     - authToken
    """
    self.send_createCredential(xiaomiAppId, appUserAuthProvider, authToken)
    return self.recv_createCredential()

  def send_createCredential(self, xiaomiAppId, appUserAuthProvider, authToken):
    self._oprot.writeMessageBegin('createCredential', TMessageType.CALL, self._seqid)
    args = createCredential_args()
    args.xiaomiAppId = xiaomiAppId
    args.appUserAuthProvider = appUserAuthProvider
    args.authToken = authToken
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createCredential(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = createCredential_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.se is not None:
      raise result.se
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createCredential failed: unknown result");


class Processor(rpc.common.BaseService.Processor, Iface, TProcessor):
  def __init__(self, handler):
    rpc.common.BaseService.Processor.__init__(self, handler)
    self._processMap["createCredential"] = Processor.process_createCredential

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_createCredential(self, seqid, iprot, oprot):
    args = createCredential_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createCredential_result()
    try:
      result.success = self._handler.createCredential(args.xiaomiAppId, args.appUserAuthProvider, args.authToken)
    except rpc.errors.ttypes.ServiceException as se:
      result.se = se
    oprot.writeMessageBegin("createCredential", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class createCredential_args(object):
  """
  Attributes:
   - xiaomiAppId
   - appUserAuthProvider
   - authToken
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'xiaomiAppId', None, None, ), # 1
    (2, TType.I32, 'appUserAuthProvider', None, None, ), # 2
    (3, TType.STRING, 'authToken', None, None, ), # 3
  )

  def __init__(self, xiaomiAppId=None, appUserAuthProvider=None, authToken=None,):
    self.xiaomiAppId = xiaomiAppId
    self.appUserAuthProvider = appUserAuthProvider
    self.authToken = authToken

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
          self.xiaomiAppId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.appUserAuthProvider = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.authToken = iprot.readString();
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
    oprot.writeStructBegin('createCredential_args')
    if self.xiaomiAppId is not None:
      oprot.writeFieldBegin('xiaomiAppId', TType.STRING, 1)
      oprot.writeString(self.xiaomiAppId)
      oprot.writeFieldEnd()
    if self.appUserAuthProvider is not None:
      oprot.writeFieldBegin('appUserAuthProvider', TType.I32, 2)
      oprot.writeI32(self.appUserAuthProvider)
      oprot.writeFieldEnd()
    if self.authToken is not None:
      oprot.writeFieldBegin('authToken', TType.STRING, 3)
      oprot.writeString(self.authToken)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.xiaomiAppId)
    value = (value * 31) ^ hash(self.appUserAuthProvider)
    value = (value * 31) ^ hash(self.authToken)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createCredential_result(object):
  """
  Attributes:
   - success
   - se
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Credential, Credential.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'se', (rpc.errors.ttypes.ServiceException, rpc.errors.ttypes.ServiceException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, se=None,):
    self.success = success
    self.se = se

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Credential()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.se = rpc.errors.ttypes.ServiceException()
          self.se.read(iprot)
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
    oprot.writeStructBegin('createCredential_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.se is not None:
      oprot.writeFieldBegin('se', TType.STRUCT, 1)
      self.se.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.se)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.items()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
