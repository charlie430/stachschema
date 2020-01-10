# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fds/protobuf/stach/table/Wrappers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fds/protobuf/stach/table/Wrappers.proto',
  package='factset.protobuf.stach.table',
  syntax='proto3',
  serialized_options=_b('\n com.factset.protobuf.stach.tableB\rWrappersProto\252\002\034FactSet.Protobuf.Stach.Table'),
  serialized_pb=_b('\n\'fds/protobuf/stach/table/Wrappers.proto\x12\x1c\x66\x61\x63tset.protobuf.stach.table\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1d\n\x0b\x44oubleArray\x12\x0e\n\x06values\x18\x01 \x03(\x01\"\x1c\n\nFloatArray\x12\x0e\n\x06values\x18\x01 \x03(\x02\"\x1c\n\nInt32Array\x12\x0e\n\x06values\x18\x01 \x03(\x05\"\x1c\n\nInt64Array\x12\x0e\n\x06values\x18\x01 \x03(\x03\"\x1b\n\tBoolArray\x12\x0e\n\x06values\x18\x01 \x03(\x08\"\x1d\n\x0bStringArray\x12\x0e\n\x06values\x18\x01 \x03(\t\":\n\rDurationArray\x12)\n\x06values\x18\x01 \x03(\x0b\x32\x19.google.protobuf.Duration\"<\n\x0eTimestampArray\x12*\n\x06values\x18\x01 \x03(\x0b\x32\x1a.google.protobuf.TimestampBP\n com.factset.protobuf.stach.tableB\rWrappersProto\xaa\x02\x1c\x46\x61\x63tSet.Protobuf.Stach.Tableb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_DOUBLEARRAY = _descriptor.Descriptor(
  name='DoubleArray',
  full_name='factset.protobuf.stach.table.DoubleArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.DoubleArray.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=138,
  serialized_end=167,
)


_FLOATARRAY = _descriptor.Descriptor(
  name='FloatArray',
  full_name='factset.protobuf.stach.table.FloatArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.FloatArray.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=169,
  serialized_end=197,
)


_INT32ARRAY = _descriptor.Descriptor(
  name='Int32Array',
  full_name='factset.protobuf.stach.table.Int32Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.Int32Array.values', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=199,
  serialized_end=227,
)


_INT64ARRAY = _descriptor.Descriptor(
  name='Int64Array',
  full_name='factset.protobuf.stach.table.Int64Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.Int64Array.values', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=229,
  serialized_end=257,
)


_BOOLARRAY = _descriptor.Descriptor(
  name='BoolArray',
  full_name='factset.protobuf.stach.table.BoolArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.BoolArray.values', index=0,
      number=1, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=259,
  serialized_end=286,
)


_STRINGARRAY = _descriptor.Descriptor(
  name='StringArray',
  full_name='factset.protobuf.stach.table.StringArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.StringArray.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=288,
  serialized_end=317,
)


_DURATIONARRAY = _descriptor.Descriptor(
  name='DurationArray',
  full_name='factset.protobuf.stach.table.DurationArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.DurationArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=319,
  serialized_end=377,
)


_TIMESTAMPARRAY = _descriptor.Descriptor(
  name='TimestampArray',
  full_name='factset.protobuf.stach.table.TimestampArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='factset.protobuf.stach.table.TimestampArray.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=379,
  serialized_end=439,
)

_DURATIONARRAY.fields_by_name['values'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TIMESTAMPARRAY.fields_by_name['values'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['DoubleArray'] = _DOUBLEARRAY
DESCRIPTOR.message_types_by_name['FloatArray'] = _FLOATARRAY
DESCRIPTOR.message_types_by_name['Int32Array'] = _INT32ARRAY
DESCRIPTOR.message_types_by_name['Int64Array'] = _INT64ARRAY
DESCRIPTOR.message_types_by_name['BoolArray'] = _BOOLARRAY
DESCRIPTOR.message_types_by_name['StringArray'] = _STRINGARRAY
DESCRIPTOR.message_types_by_name['DurationArray'] = _DURATIONARRAY
DESCRIPTOR.message_types_by_name['TimestampArray'] = _TIMESTAMPARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoubleArray = _reflection.GeneratedProtocolMessageType('DoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.DoubleArray)
  })
_sym_db.RegisterMessage(DoubleArray)

FloatArray = _reflection.GeneratedProtocolMessageType('FloatArray', (_message.Message,), {
  'DESCRIPTOR' : _FLOATARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.FloatArray)
  })
_sym_db.RegisterMessage(FloatArray)

Int32Array = _reflection.GeneratedProtocolMessageType('Int32Array', (_message.Message,), {
  'DESCRIPTOR' : _INT32ARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.Int32Array)
  })
_sym_db.RegisterMessage(Int32Array)

Int64Array = _reflection.GeneratedProtocolMessageType('Int64Array', (_message.Message,), {
  'DESCRIPTOR' : _INT64ARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.Int64Array)
  })
_sym_db.RegisterMessage(Int64Array)

BoolArray = _reflection.GeneratedProtocolMessageType('BoolArray', (_message.Message,), {
  'DESCRIPTOR' : _BOOLARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.BoolArray)
  })
_sym_db.RegisterMessage(BoolArray)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.StringArray)
  })
_sym_db.RegisterMessage(StringArray)

DurationArray = _reflection.GeneratedProtocolMessageType('DurationArray', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.DurationArray)
  })
_sym_db.RegisterMessage(DurationArray)

TimestampArray = _reflection.GeneratedProtocolMessageType('TimestampArray', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMPARRAY,
  '__module__' : 'fds.protobuf.stach.table.Wrappers_pb2'
  # @@protoc_insertion_point(class_scope:factset.protobuf.stach.table.TimestampArray)
  })
_sym_db.RegisterMessage(TimestampArray)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
