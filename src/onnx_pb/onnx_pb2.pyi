from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
EXPERIMENTAL: OperatorStatus
IR_VERSION: Version
IR_VERSION_2017_10_10: Version
IR_VERSION_2017_10_30: Version
IR_VERSION_2017_11_3: Version
IR_VERSION_2019_1_22: Version
IR_VERSION_2019_3_18: Version
IR_VERSION_2019_9_19: Version
IR_VERSION_2020_5_8: Version
IR_VERSION_2021_7_30: Version
IR_VERSION_2023_5_5: Version
STABLE: OperatorStatus
_START_VERSION: Version

class AttributeProto(_message.Message):
    __slots__ = ["doc_string", "f", "floats", "g", "graphs", "i", "ints", "name", "ref_attr_name", "s", "sparse_tensor", "sparse_tensors", "strings", "t", "tensors", "tp", "type", "type_protos"]
    class AttributeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    FLOAT: AttributeProto.AttributeType
    FLOATS: AttributeProto.AttributeType
    FLOATS_FIELD_NUMBER: ClassVar[int]
    F_FIELD_NUMBER: ClassVar[int]
    GRAPH: AttributeProto.AttributeType
    GRAPHS: AttributeProto.AttributeType
    GRAPHS_FIELD_NUMBER: ClassVar[int]
    G_FIELD_NUMBER: ClassVar[int]
    INT: AttributeProto.AttributeType
    INTS: AttributeProto.AttributeType
    INTS_FIELD_NUMBER: ClassVar[int]
    I_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    REF_ATTR_NAME_FIELD_NUMBER: ClassVar[int]
    SPARSE_TENSOR: AttributeProto.AttributeType
    SPARSE_TENSORS: AttributeProto.AttributeType
    SPARSE_TENSORS_FIELD_NUMBER: ClassVar[int]
    SPARSE_TENSOR_FIELD_NUMBER: ClassVar[int]
    STRING: AttributeProto.AttributeType
    STRINGS: AttributeProto.AttributeType
    STRINGS_FIELD_NUMBER: ClassVar[int]
    S_FIELD_NUMBER: ClassVar[int]
    TENSOR: AttributeProto.AttributeType
    TENSORS: AttributeProto.AttributeType
    TENSORS_FIELD_NUMBER: ClassVar[int]
    TP_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    TYPE_PROTO: AttributeProto.AttributeType
    TYPE_PROTOS: AttributeProto.AttributeType
    TYPE_PROTOS_FIELD_NUMBER: ClassVar[int]
    T_FIELD_NUMBER: ClassVar[int]
    UNDEFINED: AttributeProto.AttributeType
    doc_string: str
    f: float
    floats: _containers.RepeatedScalarFieldContainer[float]
    g: GraphProto
    graphs: _containers.RepeatedCompositeFieldContainer[GraphProto]
    i: int
    ints: _containers.RepeatedScalarFieldContainer[int]
    name: str
    ref_attr_name: str
    s: bytes
    sparse_tensor: SparseTensorProto
    sparse_tensors: _containers.RepeatedCompositeFieldContainer[SparseTensorProto]
    strings: _containers.RepeatedScalarFieldContainer[bytes]
    t: TensorProto
    tensors: _containers.RepeatedCompositeFieldContainer[TensorProto]
    tp: TypeProto
    type: AttributeProto.AttributeType
    type_protos: _containers.RepeatedCompositeFieldContainer[TypeProto]
    def __init__(self, name: Optional[str] = ..., ref_attr_name: Optional[str] = ..., doc_string: Optional[str] = ..., type: Optional[Union[AttributeProto.AttributeType, str]] = ..., f: Optional[float] = ..., i: Optional[int] = ..., s: Optional[bytes] = ..., t: Optional[Union[TensorProto, Mapping]] = ..., g: Optional[Union[GraphProto, Mapping]] = ..., sparse_tensor: Optional[Union[SparseTensorProto, Mapping]] = ..., tp: Optional[Union[TypeProto, Mapping]] = ..., floats: Optional[Iterable[float]] = ..., ints: Optional[Iterable[int]] = ..., strings: Optional[Iterable[bytes]] = ..., tensors: Optional[Iterable[Union[TensorProto, Mapping]]] = ..., graphs: Optional[Iterable[Union[GraphProto, Mapping]]] = ..., sparse_tensors: Optional[Iterable[Union[SparseTensorProto, Mapping]]] = ..., type_protos: Optional[Iterable[Union[TypeProto, Mapping]]] = ...) -> None: ...

class FunctionProto(_message.Message):
    __slots__ = ["attribute", "attribute_proto", "doc_string", "domain", "input", "metadata_props", "name", "node", "opset_import", "output", "overload", "value_info"]
    ATTRIBUTE_FIELD_NUMBER: ClassVar[int]
    ATTRIBUTE_PROTO_FIELD_NUMBER: ClassVar[int]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    DOMAIN_FIELD_NUMBER: ClassVar[int]
    INPUT_FIELD_NUMBER: ClassVar[int]
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    NODE_FIELD_NUMBER: ClassVar[int]
    OPSET_IMPORT_FIELD_NUMBER: ClassVar[int]
    OUTPUT_FIELD_NUMBER: ClassVar[int]
    OVERLOAD_FIELD_NUMBER: ClassVar[int]
    VALUE_INFO_FIELD_NUMBER: ClassVar[int]
    attribute: _containers.RepeatedScalarFieldContainer[str]
    attribute_proto: _containers.RepeatedCompositeFieldContainer[AttributeProto]
    doc_string: str
    domain: str
    input: _containers.RepeatedScalarFieldContainer[str]
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    name: str
    node: _containers.RepeatedCompositeFieldContainer[NodeProto]
    opset_import: _containers.RepeatedCompositeFieldContainer[OperatorSetIdProto]
    output: _containers.RepeatedScalarFieldContainer[str]
    overload: str
    value_info: _containers.RepeatedCompositeFieldContainer[ValueInfoProto]
    def __init__(self, name: Optional[str] = ..., input: Optional[Iterable[str]] = ..., output: Optional[Iterable[str]] = ..., attribute: Optional[Iterable[str]] = ..., attribute_proto: Optional[Iterable[Union[AttributeProto, Mapping]]] = ..., node: Optional[Iterable[Union[NodeProto, Mapping]]] = ..., doc_string: Optional[str] = ..., opset_import: Optional[Iterable[Union[OperatorSetIdProto, Mapping]]] = ..., domain: Optional[str] = ..., overload: Optional[str] = ..., value_info: Optional[Iterable[Union[ValueInfoProto, Mapping]]] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class GraphProto(_message.Message):
    __slots__ = ["doc_string", "initializer", "input", "metadata_props", "name", "node", "output", "quantization_annotation", "sparse_initializer", "value_info"]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    INITIALIZER_FIELD_NUMBER: ClassVar[int]
    INPUT_FIELD_NUMBER: ClassVar[int]
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    NODE_FIELD_NUMBER: ClassVar[int]
    OUTPUT_FIELD_NUMBER: ClassVar[int]
    QUANTIZATION_ANNOTATION_FIELD_NUMBER: ClassVar[int]
    SPARSE_INITIALIZER_FIELD_NUMBER: ClassVar[int]
    VALUE_INFO_FIELD_NUMBER: ClassVar[int]
    doc_string: str
    initializer: _containers.RepeatedCompositeFieldContainer[TensorProto]
    input: _containers.RepeatedCompositeFieldContainer[ValueInfoProto]
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    name: str
    node: _containers.RepeatedCompositeFieldContainer[NodeProto]
    output: _containers.RepeatedCompositeFieldContainer[ValueInfoProto]
    quantization_annotation: _containers.RepeatedCompositeFieldContainer[TensorAnnotation]
    sparse_initializer: _containers.RepeatedCompositeFieldContainer[SparseTensorProto]
    value_info: _containers.RepeatedCompositeFieldContainer[ValueInfoProto]
    def __init__(self, node: Optional[Iterable[Union[NodeProto, Mapping]]] = ..., name: Optional[str] = ..., initializer: Optional[Iterable[Union[TensorProto, Mapping]]] = ..., sparse_initializer: Optional[Iterable[Union[SparseTensorProto, Mapping]]] = ..., doc_string: Optional[str] = ..., input: Optional[Iterable[Union[ValueInfoProto, Mapping]]] = ..., output: Optional[Iterable[Union[ValueInfoProto, Mapping]]] = ..., value_info: Optional[Iterable[Union[ValueInfoProto, Mapping]]] = ..., quantization_annotation: Optional[Iterable[Union[TensorAnnotation, Mapping]]] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class ModelProto(_message.Message):
    __slots__ = ["doc_string", "domain", "functions", "graph", "ir_version", "metadata_props", "model_version", "opset_import", "producer_name", "producer_version", "training_info"]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    DOMAIN_FIELD_NUMBER: ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: ClassVar[int]
    GRAPH_FIELD_NUMBER: ClassVar[int]
    IR_VERSION_FIELD_NUMBER: ClassVar[int]
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: ClassVar[int]
    OPSET_IMPORT_FIELD_NUMBER: ClassVar[int]
    PRODUCER_NAME_FIELD_NUMBER: ClassVar[int]
    PRODUCER_VERSION_FIELD_NUMBER: ClassVar[int]
    TRAINING_INFO_FIELD_NUMBER: ClassVar[int]
    doc_string: str
    domain: str
    functions: _containers.RepeatedCompositeFieldContainer[FunctionProto]
    graph: GraphProto
    ir_version: int
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    model_version: int
    opset_import: _containers.RepeatedCompositeFieldContainer[OperatorSetIdProto]
    producer_name: str
    producer_version: str
    training_info: _containers.RepeatedCompositeFieldContainer[TrainingInfoProto]
    def __init__(self, ir_version: Optional[int] = ..., opset_import: Optional[Iterable[Union[OperatorSetIdProto, Mapping]]] = ..., producer_name: Optional[str] = ..., producer_version: Optional[str] = ..., domain: Optional[str] = ..., model_version: Optional[int] = ..., doc_string: Optional[str] = ..., graph: Optional[Union[GraphProto, Mapping]] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ..., training_info: Optional[Iterable[Union[TrainingInfoProto, Mapping]]] = ..., functions: Optional[Iterable[Union[FunctionProto, Mapping]]] = ...) -> None: ...

class NodeProto(_message.Message):
    __slots__ = ["attribute", "doc_string", "domain", "input", "metadata_props", "name", "op_type", "output", "overload"]
    ATTRIBUTE_FIELD_NUMBER: ClassVar[int]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    DOMAIN_FIELD_NUMBER: ClassVar[int]
    INPUT_FIELD_NUMBER: ClassVar[int]
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OP_TYPE_FIELD_NUMBER: ClassVar[int]
    OUTPUT_FIELD_NUMBER: ClassVar[int]
    OVERLOAD_FIELD_NUMBER: ClassVar[int]
    attribute: _containers.RepeatedCompositeFieldContainer[AttributeProto]
    doc_string: str
    domain: str
    input: _containers.RepeatedScalarFieldContainer[str]
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    name: str
    op_type: str
    output: _containers.RepeatedScalarFieldContainer[str]
    overload: str
    def __init__(self, input: Optional[Iterable[str]] = ..., output: Optional[Iterable[str]] = ..., name: Optional[str] = ..., op_type: Optional[str] = ..., domain: Optional[str] = ..., overload: Optional[str] = ..., attribute: Optional[Iterable[Union[AttributeProto, Mapping]]] = ..., doc_string: Optional[str] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class OperatorSetIdProto(_message.Message):
    __slots__ = ["domain", "version"]
    DOMAIN_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    domain: str
    version: int
    def __init__(self, domain: Optional[str] = ..., version: Optional[int] = ...) -> None: ...

class SparseTensorProto(_message.Message):
    __slots__ = ["dims", "indices", "values"]
    DIMS_FIELD_NUMBER: ClassVar[int]
    INDICES_FIELD_NUMBER: ClassVar[int]
    VALUES_FIELD_NUMBER: ClassVar[int]
    dims: _containers.RepeatedScalarFieldContainer[int]
    indices: TensorProto
    values: TensorProto
    def __init__(self, values: Optional[Union[TensorProto, Mapping]] = ..., indices: Optional[Union[TensorProto, Mapping]] = ..., dims: Optional[Iterable[int]] = ...) -> None: ...

class StringStringEntryProto(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    key: str
    value: str
    def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...

class TensorAnnotation(_message.Message):
    __slots__ = ["quant_parameter_tensor_names", "tensor_name"]
    QUANT_PARAMETER_TENSOR_NAMES_FIELD_NUMBER: ClassVar[int]
    TENSOR_NAME_FIELD_NUMBER: ClassVar[int]
    quant_parameter_tensor_names: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    tensor_name: str
    def __init__(self, tensor_name: Optional[str] = ..., quant_parameter_tensor_names: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class TensorProto(_message.Message):
    __slots__ = ["data_location", "data_type", "dims", "doc_string", "double_data", "external_data", "float_data", "int32_data", "int64_data", "metadata_props", "name", "raw_data", "segment", "string_data", "uint64_data"]
    class DataLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Segment(_message.Message):
        __slots__ = ["begin", "end"]
        BEGIN_FIELD_NUMBER: ClassVar[int]
        END_FIELD_NUMBER: ClassVar[int]
        begin: int
        end: int
        def __init__(self, begin: Optional[int] = ..., end: Optional[int] = ...) -> None: ...
    BFLOAT16: TensorProto.DataType
    BOOL: TensorProto.DataType
    COMPLEX128: TensorProto.DataType
    COMPLEX64: TensorProto.DataType
    DATA_LOCATION_FIELD_NUMBER: ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: ClassVar[int]
    DEFAULT: TensorProto.DataLocation
    DIMS_FIELD_NUMBER: ClassVar[int]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    DOUBLE: TensorProto.DataType
    DOUBLE_DATA_FIELD_NUMBER: ClassVar[int]
    EXTERNAL: TensorProto.DataLocation
    EXTERNAL_DATA_FIELD_NUMBER: ClassVar[int]
    FLOAT: TensorProto.DataType
    FLOAT16: TensorProto.DataType
    FLOAT8E4M3FN: TensorProto.DataType
    FLOAT8E4M3FNUZ: TensorProto.DataType
    FLOAT8E5M2: TensorProto.DataType
    FLOAT8E5M2FNUZ: TensorProto.DataType
    FLOAT_DATA_FIELD_NUMBER: ClassVar[int]
    INT16: TensorProto.DataType
    INT32: TensorProto.DataType
    INT32_DATA_FIELD_NUMBER: ClassVar[int]
    INT4: TensorProto.DataType
    INT64: TensorProto.DataType
    INT64_DATA_FIELD_NUMBER: ClassVar[int]
    INT8: TensorProto.DataType
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    RAW_DATA_FIELD_NUMBER: ClassVar[int]
    SEGMENT_FIELD_NUMBER: ClassVar[int]
    STRING: TensorProto.DataType
    STRING_DATA_FIELD_NUMBER: ClassVar[int]
    UINT16: TensorProto.DataType
    UINT32: TensorProto.DataType
    UINT4: TensorProto.DataType
    UINT64: TensorProto.DataType
    UINT64_DATA_FIELD_NUMBER: ClassVar[int]
    UINT8: TensorProto.DataType
    UNDEFINED: TensorProto.DataType
    data_location: TensorProto.DataLocation
    data_type: int
    dims: _containers.RepeatedScalarFieldContainer[int]
    doc_string: str
    double_data: _containers.RepeatedScalarFieldContainer[float]
    external_data: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    float_data: _containers.RepeatedScalarFieldContainer[float]
    int32_data: _containers.RepeatedScalarFieldContainer[int]
    int64_data: _containers.RepeatedScalarFieldContainer[int]
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    name: str
    raw_data: bytes
    segment: TensorProto.Segment
    string_data: _containers.RepeatedScalarFieldContainer[bytes]
    uint64_data: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dims: Optional[Iterable[int]] = ..., data_type: Optional[int] = ..., segment: Optional[Union[TensorProto.Segment, Mapping]] = ..., float_data: Optional[Iterable[float]] = ..., int32_data: Optional[Iterable[int]] = ..., string_data: Optional[Iterable[bytes]] = ..., int64_data: Optional[Iterable[int]] = ..., name: Optional[str] = ..., doc_string: Optional[str] = ..., raw_data: Optional[bytes] = ..., external_data: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ..., data_location: Optional[Union[TensorProto.DataLocation, str]] = ..., double_data: Optional[Iterable[float]] = ..., uint64_data: Optional[Iterable[int]] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class TensorShapeProto(_message.Message):
    __slots__ = ["dim"]
    class Dimension(_message.Message):
        __slots__ = ["denotation", "dim_param", "dim_value"]
        DENOTATION_FIELD_NUMBER: ClassVar[int]
        DIM_PARAM_FIELD_NUMBER: ClassVar[int]
        DIM_VALUE_FIELD_NUMBER: ClassVar[int]
        denotation: str
        dim_param: str
        dim_value: int
        def __init__(self, dim_value: Optional[int] = ..., dim_param: Optional[str] = ..., denotation: Optional[str] = ...) -> None: ...
    DIM_FIELD_NUMBER: ClassVar[int]
    dim: _containers.RepeatedCompositeFieldContainer[TensorShapeProto.Dimension]
    def __init__(self, dim: Optional[Iterable[Union[TensorShapeProto.Dimension, Mapping]]] = ...) -> None: ...

class TrainingInfoProto(_message.Message):
    __slots__ = ["algorithm", "initialization", "initialization_binding", "update_binding"]
    ALGORITHM_FIELD_NUMBER: ClassVar[int]
    INITIALIZATION_BINDING_FIELD_NUMBER: ClassVar[int]
    INITIALIZATION_FIELD_NUMBER: ClassVar[int]
    UPDATE_BINDING_FIELD_NUMBER: ClassVar[int]
    algorithm: GraphProto
    initialization: GraphProto
    initialization_binding: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    update_binding: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    def __init__(self, initialization: Optional[Union[GraphProto, Mapping]] = ..., algorithm: Optional[Union[GraphProto, Mapping]] = ..., initialization_binding: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ..., update_binding: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class TypeProto(_message.Message):
    __slots__ = ["denotation", "map_type", "optional_type", "sequence_type", "sparse_tensor_type", "tensor_type"]
    class Map(_message.Message):
        __slots__ = ["key_type", "value_type"]
        KEY_TYPE_FIELD_NUMBER: ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: ClassVar[int]
        key_type: int
        value_type: TypeProto
        def __init__(self, key_type: Optional[int] = ..., value_type: Optional[Union[TypeProto, Mapping]] = ...) -> None: ...
    class Optional(_message.Message):
        __slots__ = ["elem_type"]
        ELEM_TYPE_FIELD_NUMBER: ClassVar[int]
        elem_type: TypeProto
        def __init__(self, elem_type: Optional[Union[TypeProto, Mapping]] = ...) -> None: ...
    class Sequence(_message.Message):
        __slots__ = ["elem_type"]
        ELEM_TYPE_FIELD_NUMBER: ClassVar[int]
        elem_type: TypeProto
        def __init__(self, elem_type: Optional[Union[TypeProto, Mapping]] = ...) -> None: ...
    class SparseTensor(_message.Message):
        __slots__ = ["elem_type", "shape"]
        ELEM_TYPE_FIELD_NUMBER: ClassVar[int]
        SHAPE_FIELD_NUMBER: ClassVar[int]
        elem_type: int
        shape: TensorShapeProto
        def __init__(self, elem_type: Optional[int] = ..., shape: Optional[Union[TensorShapeProto, Mapping]] = ...) -> None: ...
    class Tensor(_message.Message):
        __slots__ = ["elem_type", "shape"]
        ELEM_TYPE_FIELD_NUMBER: ClassVar[int]
        SHAPE_FIELD_NUMBER: ClassVar[int]
        elem_type: int
        shape: TensorShapeProto
        def __init__(self, elem_type: Optional[int] = ..., shape: Optional[Union[TensorShapeProto, Mapping]] = ...) -> None: ...
    DENOTATION_FIELD_NUMBER: ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: ClassVar[int]
    OPTIONAL_TYPE_FIELD_NUMBER: ClassVar[int]
    SEQUENCE_TYPE_FIELD_NUMBER: ClassVar[int]
    SPARSE_TENSOR_TYPE_FIELD_NUMBER: ClassVar[int]
    TENSOR_TYPE_FIELD_NUMBER: ClassVar[int]
    denotation: str
    map_type: TypeProto.Map
    optional_type: TypeProto.Optional
    sequence_type: TypeProto.Sequence
    sparse_tensor_type: TypeProto.SparseTensor
    tensor_type: TypeProto.Tensor
    def __init__(self, tensor_type: Optional[Union[TypeProto.Tensor, Mapping]] = ..., sequence_type: Optional[Union[TypeProto.Sequence, Mapping]] = ..., map_type: Optional[Union[TypeProto.Map, Mapping]] = ..., optional_type: Optional[Union[TypeProto.Optional, Mapping]] = ..., sparse_tensor_type: Optional[Union[TypeProto.SparseTensor, Mapping]] = ..., denotation: Optional[str] = ...) -> None: ...

class ValueInfoProto(_message.Message):
    __slots__ = ["doc_string", "metadata_props", "name", "type"]
    DOC_STRING_FIELD_NUMBER: ClassVar[int]
    METADATA_PROPS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    doc_string: str
    metadata_props: _containers.RepeatedCompositeFieldContainer[StringStringEntryProto]
    name: str
    type: TypeProto
    def __init__(self, name: Optional[str] = ..., type: Optional[Union[TypeProto, Mapping]] = ..., doc_string: Optional[str] = ..., metadata_props: Optional[Iterable[Union[StringStringEntryProto, Mapping]]] = ...) -> None: ...

class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OperatorStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
