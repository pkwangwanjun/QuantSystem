# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ndata.proto\x12\x07\x65xample\"f\n\x05Stock\x12\x0e\n\x06\x64irect\x18\x01 \x01(\t\x12\x12\n\nindex_code\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\"d\n\x03Rlt\x12\x0e\n\x06\x64irect\x18\x01 \x01(\t\x12\x12\n\nindex_code\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x05\x12\x0c\n\x04type\x18\x06 \x01(\x05\x32\x38\n\nFormatData\x12*\n\x08\x44oFormat\x12\x0e.example.Stock\x1a\x0c.example.Rlt\"\x00\x62\x06proto3')
)




_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='example.Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direct', full_name='example.Stock.direct', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_code', full_name='example.Stock.index_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='example.Stock.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='example.Stock.price', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='example.Stock.amount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='example.Stock.type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=125,
)


_RLT = _descriptor.Descriptor(
  name='Rlt',
  full_name='example.Rlt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direct', full_name='example.Rlt.direct', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_code', full_name='example.Rlt.index_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='example.Rlt.time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='example.Rlt.price', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='example.Rlt.amount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='example.Rlt.type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=227,
)

DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['Rlt'] = _RLT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Stock = _reflection.GeneratedProtocolMessageType('Stock', (_message.Message,), {
  'DESCRIPTOR' : _STOCK,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:example.Stock)
  })
_sym_db.RegisterMessage(Stock)

Rlt = _reflection.GeneratedProtocolMessageType('Rlt', (_message.Message,), {
  'DESCRIPTOR' : _RLT,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:example.Rlt)
  })
_sym_db.RegisterMessage(Rlt)



_FORMATDATA = _descriptor.ServiceDescriptor(
  name='FormatData',
  full_name='example.FormatData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=229,
  serialized_end=285,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoFormat',
    full_name='example.FormatData.DoFormat',
    index=0,
    containing_service=None,
    input_type=_STOCK,
    output_type=_RLT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORMATDATA)

DESCRIPTOR.services_by_name['FormatData'] = _FORMATDATA

# @@protoc_insertion_point(module_scope)
