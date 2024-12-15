import rhinoscriptsyntax as rs
import itertools

block_names = rs.BlockNames()

# rs.BlockContainerCount excludes nested blocks, but doesn't work
# in externally linked blocks - WARNING! ">" character can be used
# on filenames in Linux
block_names_not_nested = [block_name for block_name in block_names 
                            if rs.BlockContainerCount(block_name) == 0
                            and ">" not in block_name]

selected_blocks = rs.MultiListBox(sorted(block_names_not_nested))
block_instances = [rs.BlockInstances(selected_block) for selected_block in selected_blocks]
# https://stackoverflow.com/a/953097 - unpacking lists in python
block_instances_unpacked = list(itertools.chain(*block_instances))
rs.SelectObjects(block_instances_unpacked)