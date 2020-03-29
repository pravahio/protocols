# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health/Covid19District.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import FeedHeader_pb2 as FeedHeader__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='health/Covid19District.proto',
  package='health_covid_district',
  syntax='proto3',
  serialized_options=b'\n\037io.pravah.health.covid_district',
  serialized_pb=b'\n\x1chealth/Covid19District.proto\x12\x15health_covid_district\x1a\x10\x46\x65\x65\x64Header.proto\"]\n\x0b\x46\x65\x65\x64Message\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.FeedHeader\x12\x31\n\tcountries\x18\x02 \x03(\x0b\x32\x1e.health_covid_district.Country\"r\n\x07\x43ountry\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12+\n\x05stats\x18\x02 \x01(\x0b\x32\x1c.health_covid_district.Stats\x12,\n\x06states\x18\x03 \x03(\x0b\x32\x1c.health_covid_district.State\"v\n\x05State\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12+\n\x05stats\x18\x02 \x01(\x0b\x32\x1c.health_covid_district.Stats\x12\x32\n\tdistricts\x18\x03 \x03(\x0b\x32\x1f.health_covid_district.District\"y\n\x08\x44istrict\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12+\n\x05stats\x18\x02 \x01(\x0b\x32\x1c.health_covid_district.Stats\x12\x32\n\thospitals\x18\x03 \x03(\x0b\x32\x1f.health_covid_district.Hospital\"w\n\x08Hospital\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12+\n\x05stats\x18\x02 \x01(\x0b\x32\x1c.health_covid_district.Stats\x12\x30\n\x08patients\x18\x03 \x03(\x0b\x32\x1e.health_covid_district.Patient\"|\n\x05Stats\x12\x1a\n\x12totalPositiveCases\x18\x01 \x01(\r\x12\x1b\n\x13\x61\x63tivePositiveCases\x18\x02 \x01(\r\x12\x12\n\ncuredCases\x18\x03 \x01(\r\x12\x12\n\ndeathCases\x18\x04 \x01(\r\x12\x12\n\notherCases\x18\x05 \x01(\r\"f\n\x07Patient\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\r\x12\x0e\n\x06gender\x18\x03 \x01(\t\x12\x16\n\x0einfectedOnDate\x18\x04 \x01(\x04\x12\x18\n\x10infectedFromUUID\x18\x05 \x03(\tB!\n\x1fio.pravah.health.covid_districtb\x06proto3'
  ,
  dependencies=[FeedHeader__pb2.DESCRIPTOR,])




_FEEDMESSAGE = _descriptor.Descriptor(
  name='FeedMessage',
  full_name='health_covid_district.FeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='health_covid_district.FeedMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries', full_name='health_covid_district.FeedMessage.countries', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=73,
  serialized_end=166,
)


_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='health_covid_district.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_covid_district.Country.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='health_covid_district.Country.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='states', full_name='health_covid_district.Country.states', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=168,
  serialized_end=282,
)


_STATE = _descriptor.Descriptor(
  name='State',
  full_name='health_covid_district.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_covid_district.State.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='health_covid_district.State.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='districts', full_name='health_covid_district.State.districts', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=284,
  serialized_end=402,
)


_DISTRICT = _descriptor.Descriptor(
  name='District',
  full_name='health_covid_district.District',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_covid_district.District.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='health_covid_district.District.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hospitals', full_name='health_covid_district.District.hospitals', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=404,
  serialized_end=525,
)


_HOSPITAL = _descriptor.Descriptor(
  name='Hospital',
  full_name='health_covid_district.Hospital',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='health_covid_district.Hospital.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='health_covid_district.Hospital.stats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patients', full_name='health_covid_district.Hospital.patients', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=527,
  serialized_end=646,
)


_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='health_covid_district.Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalPositiveCases', full_name='health_covid_district.Stats.totalPositiveCases', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activePositiveCases', full_name='health_covid_district.Stats.activePositiveCases', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='curedCases', full_name='health_covid_district.Stats.curedCases', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deathCases', full_name='health_covid_district.Stats.deathCases', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otherCases', full_name='health_covid_district.Stats.otherCases', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=648,
  serialized_end=772,
)


_PATIENT = _descriptor.Descriptor(
  name='Patient',
  full_name='health_covid_district.Patient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='health_covid_district.Patient.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='health_covid_district.Patient.age', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='health_covid_district.Patient.gender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infectedOnDate', full_name='health_covid_district.Patient.infectedOnDate', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infectedFromUUID', full_name='health_covid_district.Patient.infectedFromUUID', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  serialized_start=774,
  serialized_end=876,
)

_FEEDMESSAGE.fields_by_name['header'].message_type = FeedHeader__pb2._FEEDHEADER
_FEEDMESSAGE.fields_by_name['countries'].message_type = _COUNTRY
_COUNTRY.fields_by_name['stats'].message_type = _STATS
_COUNTRY.fields_by_name['states'].message_type = _STATE
_STATE.fields_by_name['stats'].message_type = _STATS
_STATE.fields_by_name['districts'].message_type = _DISTRICT
_DISTRICT.fields_by_name['stats'].message_type = _STATS
_DISTRICT.fields_by_name['hospitals'].message_type = _HOSPITAL
_HOSPITAL.fields_by_name['stats'].message_type = _STATS
_HOSPITAL.fields_by_name['patients'].message_type = _PATIENT
DESCRIPTOR.message_types_by_name['FeedMessage'] = _FEEDMESSAGE
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['State'] = _STATE
DESCRIPTOR.message_types_by_name['District'] = _DISTRICT
DESCRIPTOR.message_types_by_name['Hospital'] = _HOSPITAL
DESCRIPTOR.message_types_by_name['Stats'] = _STATS
DESCRIPTOR.message_types_by_name['Patient'] = _PATIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMessage = _reflection.GeneratedProtocolMessageType('FeedMessage', (_message.Message,), {
  'DESCRIPTOR' : _FEEDMESSAGE,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.FeedMessage)
  })
_sym_db.RegisterMessage(FeedMessage)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), {
  'DESCRIPTOR' : _COUNTRY,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.Country)
  })
_sym_db.RegisterMessage(Country)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
  'DESCRIPTOR' : _STATE,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.State)
  })
_sym_db.RegisterMessage(State)

District = _reflection.GeneratedProtocolMessageType('District', (_message.Message,), {
  'DESCRIPTOR' : _DISTRICT,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.District)
  })
_sym_db.RegisterMessage(District)

Hospital = _reflection.GeneratedProtocolMessageType('Hospital', (_message.Message,), {
  'DESCRIPTOR' : _HOSPITAL,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.Hospital)
  })
_sym_db.RegisterMessage(Hospital)

Stats = _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
  'DESCRIPTOR' : _STATS,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.Stats)
  })
_sym_db.RegisterMessage(Stats)

Patient = _reflection.GeneratedProtocolMessageType('Patient', (_message.Message,), {
  'DESCRIPTOR' : _PATIENT,
  '__module__' : 'health.Covid19District_pb2'
  # @@protoc_insertion_point(class_scope:health_covid_district.Patient)
  })
_sym_db.RegisterMessage(Patient)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
