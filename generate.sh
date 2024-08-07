#!/bin/bash
protoc --proto_path=onnx --python_out=src/onnx_pb  onnx.proto --pyi_out=src/onnx_pb
