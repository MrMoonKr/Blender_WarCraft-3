from .. import constants
from ..classes.WarCraft3Model import WarCraft3Model
from ..mdx_parser import binary_reader


def parse_version(data: bytes):
    r = binary_reader.Reader(data)
    version = r.getf('<I')[0]

    print("mdl version: ", version)
    if version in constants.MDX_VERSIONS:
        constants.MDX_CURRENT_VERSION = version
        return version
    else:
        print("Version %s is not supported; the model will load as %s which might cause issues"
              % (version, 800))
        return 800
        # raise Exception('unsupported MDX format version: {0}'.format(version))
