import configparser
import logging


def _read_defaults():
    import sys
    import os.path
    path = os.path.dirname(sys.argv[0])
    path = os.path.join(path, 'Images')
    settings = dict()
    settings['ImagesDirectory'] = path
    settings['count'] = 10
    settings['changeInterval'] = 300
    settings['downloadInterval'] = 3600
    return settings


def write_default_config():
    config = configparser.ConfigParser()
    config.read_dict(_read_defaults())
    try:
        config.write('settings.cfg')
    except OSError:
        logger.exception('Unable to write configuration file')


def read_config():
    settings = _read_defaults()
    try:
        with open('settings.cfg', 'r') as f:
            config_string = '[all]\n' + f.read()
    except OSError:
        logger.exception('Cannot access configuration file. Using default values.')
    else:
        config = configparser.ConfigParser()
        config.read_string(config_string)
        options = config['all']
        settings['path'] = options['ImagesDirectory']
        settings['count'] = int(options['count'])
        settings['changeInterval'] = int(options['changeInterval'])
        settings['downloadInterval'] = int(options['downloadInterval'])
    return settings


logger = logging.getLogger('glogger')
