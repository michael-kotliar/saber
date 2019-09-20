# Copyright 2019 The Johns Hopkins University Applied Physics Laboratory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cwlVersion: v1.0
class: CommandLineTool
hints:
    DockerRequirement:
        dockerPull: aplbrain/ffn-inference
baseCommand: python
arguments: ["driver.py"]
inputs:
  input:
    type: File
    inputBinding:
      position: 1
      prefix: --input_file 
  config_file:
    type: string
    inputBinding:
      position: 2
      prefix: --config_file
  bound_start:
    type: string
    inputBinding:
      position: 3
      prefix: --bound_start
  bound_stop:
    type: string
    inputBinding:
      position: 4
      prefix: --bound_stop
  outfile:
    type: string
    inputBinding:
      position: 5
      prefix: --outfile 

outputs:
  ffn_out:
    type: File
    outputBinding:
      glob: $(inputs.outfile)
