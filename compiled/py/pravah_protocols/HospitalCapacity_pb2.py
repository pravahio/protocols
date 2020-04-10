# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health/HospitalCapacity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import FeedHeader_pb2 as FeedHeader__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='health/HospitalCapacity.proto',
  package='health_hospital_capacity',
  syntax='proto3',
  serialized_options=b'\n\"io.pravah.health.hospital_capacity',
  serialized_pb=b'\n\x1dhealth/HospitalCapacity.proto\x12\x18health_hospital_capacity\x1a\x10\x46\x65\x65\x64Header.proto\"a\n\x0b\x46\x65\x65\x64Message\x12\x1b\n\x06header\x18\x01 \x01(\x0b\x32\x0b.FeedHeader\x12\x35\n\thospitals\x18\x02 \x03(\x0b\x32\".health_hospital_capacity.Hospital\"\xe9\x01\n\x08Hospital\x12\x32\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32!.health_hospital_capacity.Details\x12@\n\x0einfrastructure\x18\x02 \x01(\x0b\x32(.health_hospital_capacity.Infrastructure\x12.\n\x05staff\x18\x03 \x01(\x0b\x32\x1f.health_hospital_capacity.Staff\x12\x37\n\nequipments\x18\x04 \x03(\x0b\x32#.health_hospital_capacity.Equipment\"\xc5\x02\n\x07\x44\x65tails\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x34\n\x08location\x18\x03 \x01(\x0b\x32\".health_hospital_capacity.Location\x12>\n\townership\x18\x04 \x01(\x0e\x32+.health_hospital_capacity.Details.Ownership\x12@\n\nspeciality\x18\x05 \x01(\x0e\x32,.health_hospital_capacity.Details.Speciality\"1\n\tOwnership\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02\"3\n\nSpeciality\x12\x0b\n\x07GENERAL\x10\x00\x12\r\n\tMATERNITY\x10\x01\x12\t\n\x05\x43OVID\x10\x04\"@\n\x08Location\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x02\x12\x11\n\tlongitude\x18\x03 \x01(\x02\"?\n\x0eInfrastructure\x12-\n\x05wards\x18\x01 \x03(\x0b\x32\x1e.health_hospital_capacity.Ward\"\xe0\x01\n\x04Ward\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x32\n\x05types\x18\x02 \x03(\x0e\x32#.health_hospital_capacity.Ward.Type\x12\x14\n\x0cnumberOfBeds\x18\x03 \x01(\r\x12\x1c\n\x14numberOfOccupiedBeds\x18\x04 \x01(\r\x12\x19\n\x11\x65xtraBedsRequired\x18\x05 \x01(\r\"G\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03ICU\x10\x01\x12\r\n\tEMERGENCY\x10\x02\x12\x0b\n\x07GENERAL\x10\x03\x12\r\n\tISOLATION\x10\x04\"a\n\x05Staff\x12\x14\n\x0ctotalDoctors\x18\x01 \x01(\r\x12\x13\n\x0btotalNurses\x18\x02 \x01(\r\x12\x19\n\x11totalSupportStaff\x18\x03 \x01(\r\x12\x12\n\notherStaff\x18\x04 \x01(\r\"\xfb\x01\n\tEquipment\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x36\n\x04type\x18\x02 \x01(\x0e\x32(.health_hospital_capacity.Equipment.Type\x12\x15\n\rquantityTotal\x18\x03 \x01(\r\x12\x15\n\rquantityInUse\x18\x04 \x01(\r\x12\x1d\n\x15\x65xtraQuantityRequired\x18\x05 \x01(\r\x12\x0c\n\x04tags\x18\x06 \x03(\t\"M\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07N95MASK\x10\x01\x12\x0e\n\nVENTILATOR\x10\x02\x12\n\n\x06GLOVES\x10\x03\x12\x0f\n\x0b\x46\x41\x43\x45_SHIELD\x10\x04\x42$\n\"io.pravah.health.hospital_capacityb\x06proto3'
  ,
  dependencies=[FeedHeader__pb2.DESCRIPTOR,])



_DETAILS_OWNERSHIP = _descriptor.EnumDescriptor(
  name='Ownership',
  full_name='health_hospital_capacity.Details.Ownership',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVATE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=636,
  serialized_end=685,
)
_sym_db.RegisterEnumDescriptor(_DETAILS_OWNERSHIP)

_DETAILS_SPECIALITY = _descriptor.EnumDescriptor(
  name='Speciality',
  full_name='health_hospital_capacity.Details.Speciality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATERNITY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COVID', index=2, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=687,
  serialized_end=738,
)
_sym_db.RegisterEnumDescriptor(_DETAILS_SPECIALITY)

_WARD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='health_hospital_capacity.Ward.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ICU', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMERGENCY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERAL', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISOLATION', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1025,
  serialized_end=1096,
)
_sym_db.RegisterEnumDescriptor(_WARD_TYPE)

_EQUIPMENT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='health_hospital_capacity.Equipment.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='N95MASK', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VENTILATOR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOVES', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACE_SHIELD', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1372,
  serialized_end=1449,
)
_sym_db.RegisterEnumDescriptor(_EQUIPMENT_TYPE)


_FEEDMESSAGE = _descriptor.Descriptor(
  name='FeedMessage',
  full_name='health_hospital_capacity.FeedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='health_hospital_capacity.FeedMessage.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hospitals', full_name='health_hospital_capacity.FeedMessage.hospitals', index=1,
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
  serialized_start=77,
  serialized_end=174,
)


_HOSPITAL = _descriptor.Descriptor(
  name='Hospital',
  full_name='health_hospital_capacity.Hospital',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='health_hospital_capacity.Hospital.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infrastructure', full_name='health_hospital_capacity.Hospital.infrastructure', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='staff', full_name='health_hospital_capacity.Hospital.staff', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equipments', full_name='health_hospital_capacity.Hospital.equipments', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=177,
  serialized_end=410,
)


_DETAILS = _descriptor.Descriptor(
  name='Details',
  full_name='health_hospital_capacity.Details',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='health_hospital_capacity.Details.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='health_hospital_capacity.Details.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='health_hospital_capacity.Details.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ownership', full_name='health_hospital_capacity.Details.ownership', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speciality', full_name='health_hospital_capacity.Details.speciality', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DETAILS_OWNERSHIP,
    _DETAILS_SPECIALITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=738,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='health_hospital_capacity.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='health_hospital_capacity.Location.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='health_hospital_capacity.Location.latitude', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='health_hospital_capacity.Location.longitude', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=740,
  serialized_end=804,
)


_INFRASTRUCTURE = _descriptor.Descriptor(
  name='Infrastructure',
  full_name='health_hospital_capacity.Infrastructure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wards', full_name='health_hospital_capacity.Infrastructure.wards', index=0,
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
  serialized_start=806,
  serialized_end=869,
)


_WARD = _descriptor.Descriptor(
  name='Ward',
  full_name='health_hospital_capacity.Ward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='health_hospital_capacity.Ward.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='health_hospital_capacity.Ward.types', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberOfBeds', full_name='health_hospital_capacity.Ward.numberOfBeds', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberOfOccupiedBeds', full_name='health_hospital_capacity.Ward.numberOfOccupiedBeds', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraBedsRequired', full_name='health_hospital_capacity.Ward.extraBedsRequired', index=4,
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
    _WARD_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=1096,
)


_STAFF = _descriptor.Descriptor(
  name='Staff',
  full_name='health_hospital_capacity.Staff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalDoctors', full_name='health_hospital_capacity.Staff.totalDoctors', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalNurses', full_name='health_hospital_capacity.Staff.totalNurses', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalSupportStaff', full_name='health_hospital_capacity.Staff.totalSupportStaff', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otherStaff', full_name='health_hospital_capacity.Staff.otherStaff', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=1098,
  serialized_end=1195,
)


_EQUIPMENT = _descriptor.Descriptor(
  name='Equipment',
  full_name='health_hospital_capacity.Equipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='health_hospital_capacity.Equipment.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='health_hospital_capacity.Equipment.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantityTotal', full_name='health_hospital_capacity.Equipment.quantityTotal', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantityInUse', full_name='health_hospital_capacity.Equipment.quantityInUse', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extraQuantityRequired', full_name='health_hospital_capacity.Equipment.extraQuantityRequired', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='health_hospital_capacity.Equipment.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EQUIPMENT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1198,
  serialized_end=1449,
)

_FEEDMESSAGE.fields_by_name['header'].message_type = FeedHeader__pb2._FEEDHEADER
_FEEDMESSAGE.fields_by_name['hospitals'].message_type = _HOSPITAL
_HOSPITAL.fields_by_name['details'].message_type = _DETAILS
_HOSPITAL.fields_by_name['infrastructure'].message_type = _INFRASTRUCTURE
_HOSPITAL.fields_by_name['staff'].message_type = _STAFF
_HOSPITAL.fields_by_name['equipments'].message_type = _EQUIPMENT
_DETAILS.fields_by_name['location'].message_type = _LOCATION
_DETAILS.fields_by_name['ownership'].enum_type = _DETAILS_OWNERSHIP
_DETAILS.fields_by_name['speciality'].enum_type = _DETAILS_SPECIALITY
_DETAILS_OWNERSHIP.containing_type = _DETAILS
_DETAILS_SPECIALITY.containing_type = _DETAILS
_INFRASTRUCTURE.fields_by_name['wards'].message_type = _WARD
_WARD.fields_by_name['types'].enum_type = _WARD_TYPE
_WARD_TYPE.containing_type = _WARD
_EQUIPMENT.fields_by_name['type'].enum_type = _EQUIPMENT_TYPE
_EQUIPMENT_TYPE.containing_type = _EQUIPMENT
DESCRIPTOR.message_types_by_name['FeedMessage'] = _FEEDMESSAGE
DESCRIPTOR.message_types_by_name['Hospital'] = _HOSPITAL
DESCRIPTOR.message_types_by_name['Details'] = _DETAILS
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Infrastructure'] = _INFRASTRUCTURE
DESCRIPTOR.message_types_by_name['Ward'] = _WARD
DESCRIPTOR.message_types_by_name['Staff'] = _STAFF
DESCRIPTOR.message_types_by_name['Equipment'] = _EQUIPMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedMessage = _reflection.GeneratedProtocolMessageType('FeedMessage', (_message.Message,), {
  'DESCRIPTOR' : _FEEDMESSAGE,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.FeedMessage)
  })
_sym_db.RegisterMessage(FeedMessage)

Hospital = _reflection.GeneratedProtocolMessageType('Hospital', (_message.Message,), {
  'DESCRIPTOR' : _HOSPITAL,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Hospital)
  })
_sym_db.RegisterMessage(Hospital)

Details = _reflection.GeneratedProtocolMessageType('Details', (_message.Message,), {
  'DESCRIPTOR' : _DETAILS,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Details)
  })
_sym_db.RegisterMessage(Details)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Location)
  })
_sym_db.RegisterMessage(Location)

Infrastructure = _reflection.GeneratedProtocolMessageType('Infrastructure', (_message.Message,), {
  'DESCRIPTOR' : _INFRASTRUCTURE,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Infrastructure)
  })
_sym_db.RegisterMessage(Infrastructure)

Ward = _reflection.GeneratedProtocolMessageType('Ward', (_message.Message,), {
  'DESCRIPTOR' : _WARD,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Ward)
  })
_sym_db.RegisterMessage(Ward)

Staff = _reflection.GeneratedProtocolMessageType('Staff', (_message.Message,), {
  'DESCRIPTOR' : _STAFF,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Staff)
  })
_sym_db.RegisterMessage(Staff)

Equipment = _reflection.GeneratedProtocolMessageType('Equipment', (_message.Message,), {
  'DESCRIPTOR' : _EQUIPMENT,
  '__module__' : 'health.HospitalCapacity_pb2'
  # @@protoc_insertion_point(class_scope:health_hospital_capacity.Equipment)
  })
_sym_db.RegisterMessage(Equipment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
