# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ml2/tools/protos/prop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ml2/tools/protos/prop.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bml2/tools/protos/prop.proto\"2\n\x0ePropSatProblem\x12\x0f\n\x07\x66ormula\x18\x01 \x01(\t\x12\x0f\n\x07timeout\x18\x02 \x01(\x02\"\x8a\x01\n\x0fPropSatSolution\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x34\n\nassignment\x18\x02 \x03(\x0b\x32 .PropSatSolution.AssignmentEntry\x1a\x31\n\x0f\x41ssignmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\x1a\n\x06\x43lause\x12\x10\n\x08literals\x18\x01 \x03(\x05\";\n\tResClause\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08literals\x18\x02 \x03(\x05\x12\x10\n\x08premises\x18\x03 \x03(\x05\"u\n\nCNFFormula\x12\x10\n\x08num_vars\x18\x01 \x01(\x05\x12\x13\n\x0bnum_clauses\x18\x02 \x01(\x05\x12\x18\n\x07\x63lauses\x18\x03 \x03(\x0b\x32\x07.Clause\x12\x10\n\x08\x63omments\x18\x04 \x03(\t\x12\x14\n\x0csymbol_table\x18\x05 \x03(\t\">\n\rCNFSatProblem\x12\x1c\n\x07\x66ormula\x18\x01 \x01(\x0b\x32\x0b.CNFFormula\x12\x0f\n\x07timeout\x18\x02 \x01(\x02\"s\n\x0e\x43NFSatSolution\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x12\n\nassignment\x18\x02 \x03(\x05\x12\x1e\n\rclausal_proof\x18\x03 \x03(\x0b\x32\x07.Clause\x12\x1d\n\tres_proof\x18\x04 \x03(\x0b\x32\n.ResClauseb\x06proto3'
)




_PROPSATPROBLEM = _descriptor.Descriptor(
  name='PropSatProblem',
  full_name='PropSatProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='formula', full_name='PropSatProblem.formula', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='PropSatProblem.timeout', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=31,
  serialized_end=81,
)


_PROPSATSOLUTION_ASSIGNMENTENTRY = _descriptor.Descriptor(
  name='AssignmentEntry',
  full_name='PropSatSolution.AssignmentEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PropSatSolution.AssignmentEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PropSatSolution.AssignmentEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=222,
)

_PROPSATSOLUTION = _descriptor.Descriptor(
  name='PropSatSolution',
  full_name='PropSatSolution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='PropSatSolution.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assignment', full_name='PropSatSolution.assignment', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PROPSATSOLUTION_ASSIGNMENTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=222,
)


_CLAUSE = _descriptor.Descriptor(
  name='Clause',
  full_name='Clause',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='literals', full_name='Clause.literals', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=224,
  serialized_end=250,
)


_RESCLAUSE = _descriptor.Descriptor(
  name='ResClause',
  full_name='ResClause',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ResClause.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='literals', full_name='ResClause.literals', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='premises', full_name='ResClause.premises', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=252,
  serialized_end=311,
)


_CNFFORMULA = _descriptor.Descriptor(
  name='CNFFormula',
  full_name='CNFFormula',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_vars', full_name='CNFFormula.num_vars', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_clauses', full_name='CNFFormula.num_clauses', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clauses', full_name='CNFFormula.clauses', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comments', full_name='CNFFormula.comments', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol_table', full_name='CNFFormula.symbol_table', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=313,
  serialized_end=430,
)


_CNFSATPROBLEM = _descriptor.Descriptor(
  name='CNFSatProblem',
  full_name='CNFSatProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='formula', full_name='CNFSatProblem.formula', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='CNFSatProblem.timeout', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=432,
  serialized_end=494,
)


_CNFSATSOLUTION = _descriptor.Descriptor(
  name='CNFSatSolution',
  full_name='CNFSatSolution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='CNFSatSolution.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assignment', full_name='CNFSatSolution.assignment', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clausal_proof', full_name='CNFSatSolution.clausal_proof', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='res_proof', full_name='CNFSatSolution.res_proof', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=496,
  serialized_end=611,
)

_PROPSATSOLUTION_ASSIGNMENTENTRY.containing_type = _PROPSATSOLUTION
_PROPSATSOLUTION.fields_by_name['assignment'].message_type = _PROPSATSOLUTION_ASSIGNMENTENTRY
_CNFFORMULA.fields_by_name['clauses'].message_type = _CLAUSE
_CNFSATPROBLEM.fields_by_name['formula'].message_type = _CNFFORMULA
_CNFSATSOLUTION.fields_by_name['clausal_proof'].message_type = _CLAUSE
_CNFSATSOLUTION.fields_by_name['res_proof'].message_type = _RESCLAUSE
DESCRIPTOR.message_types_by_name['PropSatProblem'] = _PROPSATPROBLEM
DESCRIPTOR.message_types_by_name['PropSatSolution'] = _PROPSATSOLUTION
DESCRIPTOR.message_types_by_name['Clause'] = _CLAUSE
DESCRIPTOR.message_types_by_name['ResClause'] = _RESCLAUSE
DESCRIPTOR.message_types_by_name['CNFFormula'] = _CNFFORMULA
DESCRIPTOR.message_types_by_name['CNFSatProblem'] = _CNFSATPROBLEM
DESCRIPTOR.message_types_by_name['CNFSatSolution'] = _CNFSATSOLUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PropSatProblem = _reflection.GeneratedProtocolMessageType('PropSatProblem', (_message.Message,), {
  'DESCRIPTOR' : _PROPSATPROBLEM,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:PropSatProblem)
  })
_sym_db.RegisterMessage(PropSatProblem)

PropSatSolution = _reflection.GeneratedProtocolMessageType('PropSatSolution', (_message.Message,), {

  'AssignmentEntry' : _reflection.GeneratedProtocolMessageType('AssignmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _PROPSATSOLUTION_ASSIGNMENTENTRY,
    '__module__' : 'ml2.tools.protos.prop_pb2'
    # @@protoc_insertion_point(class_scope:PropSatSolution.AssignmentEntry)
    })
  ,
  'DESCRIPTOR' : _PROPSATSOLUTION,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:PropSatSolution)
  })
_sym_db.RegisterMessage(PropSatSolution)
_sym_db.RegisterMessage(PropSatSolution.AssignmentEntry)

Clause = _reflection.GeneratedProtocolMessageType('Clause', (_message.Message,), {
  'DESCRIPTOR' : _CLAUSE,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:Clause)
  })
_sym_db.RegisterMessage(Clause)

ResClause = _reflection.GeneratedProtocolMessageType('ResClause', (_message.Message,), {
  'DESCRIPTOR' : _RESCLAUSE,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:ResClause)
  })
_sym_db.RegisterMessage(ResClause)

CNFFormula = _reflection.GeneratedProtocolMessageType('CNFFormula', (_message.Message,), {
  'DESCRIPTOR' : _CNFFORMULA,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:CNFFormula)
  })
_sym_db.RegisterMessage(CNFFormula)

CNFSatProblem = _reflection.GeneratedProtocolMessageType('CNFSatProblem', (_message.Message,), {
  'DESCRIPTOR' : _CNFSATPROBLEM,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:CNFSatProblem)
  })
_sym_db.RegisterMessage(CNFSatProblem)

CNFSatSolution = _reflection.GeneratedProtocolMessageType('CNFSatSolution', (_message.Message,), {
  'DESCRIPTOR' : _CNFSATSOLUTION,
  '__module__' : 'ml2.tools.protos.prop_pb2'
  # @@protoc_insertion_point(class_scope:CNFSatSolution)
  })
_sym_db.RegisterMessage(CNFSatSolution)


_PROPSATSOLUTION_ASSIGNMENTENTRY._options = None
# @@protoc_insertion_point(module_scope)
