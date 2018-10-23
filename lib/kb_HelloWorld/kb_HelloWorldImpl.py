# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class kb_HelloWorld:
    '''
    Module Name:
    kb_HelloWorld

    Module Description:
    A KBase module: kb_HelloWorld
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com/zhlu9890/kb_HelloWorld.git"
    GIT_COMMIT_HASH = "9b2e3d4c5568c8f907eb51cf2846662a573c5983"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def printhelloworld(self, ctx, params):
        """
        :param params: instance of type "InParams" (Insert your typespec
           information here.) -> structure: parameter "phrase" of String
        :returns: instance of type "OutParams" -> structure: parameter
           "phrase" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN printhelloworld
        print "IMPL file and your phrase is: " + params['phrase'] + "\n"
        returnVal = {'phrase':params['phrase']}
        #END printhelloworld

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method printhelloworld return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
