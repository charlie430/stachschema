# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fds/protobuf/stach/table/HorizontalAlignment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fds/protobuf/stach/table/HorizontalAlignment.proto',
  package='factset.protobuf.stach.table',
  syntax='proto3',
  serialized_options=_b('\n com.factset.protobuf.stach.tableB\030HorizontalAlignmentProto\252\002\034FactSet.Protobuf.Stach.Table'),
  serialized_pb=_b('\n2fds/protobuf/stach/table/HorizontalAlignment.proto\x12\x1c\x66\x61\x63tset.protobuf.stach.table*J\n\x13HorizontalAlignment\x12\x12\n\x0eUNKNOWN_HALIGN\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\n\n\x06\x43\x45NTER\x10\x02\x12\t\n\x05RIGHT\x10\x03\x42[\n com.factset.protobuf.stach.tableB\x18HorizontalAlignmentProto\xaa\x02\x1c\x46\x61\x63tSet.Protobuf.Stach.Tableb\x06proto3')
)

_HORIZONTALALIGNMENT = _descriptor.EnumDescriptor(
  name='HorizontalAlignment',
  full_name='factset.protobuf.stach.table.HorizontalAlignment',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_HALIGN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CENTER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=84,
  serialized_end=158,
)
_sym_db.RegisterEnumDescriptor(_HORIZONTALALIGNMENT)

HorizontalAlignment = enum_type_wrapper.EnumTypeWrapper(_HORIZONTALALIGNMENT)
UNKNOWN_HALIGN = 0
LEFT = 1
CENTER = 2
RIGHT = 3


DESCRIPTOR.enum_types_by_name['HorizontalAlignment'] = _HORIZONTALALIGNMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
