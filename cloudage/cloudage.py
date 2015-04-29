#!/usr/bin/env python

import sys
import json


def find_refs(resource_name, resource_object, context=None):
    if not resource_object or type(resource_object) in [str, int, bool, type(u'')]:
        return
    elif type(resource_object) == list:
        for sub_object in resource_object:
            find_refs(resource_name=resource_name, resource_object=sub_object, context=context)
    else:
        if context == 'Tags' and 'Key' in resource_object:
            context = 'Tags:' + resource_object['Key']

        for key, value in resource_object.iteritems():
            if key == 'Ref':
                print '{resource} -> {target} [label="{context}"];'.format(
                    resource=resource_name, target=value, context=context
                )
            else:
                if key not in ['Fn::Join', 'Value']:
                    if context:
                        new_context = context + ':' + key
                    else:
                        new_context = key
                else:
                    new_context = context
                find_refs(resource_name=resource_name, resource_object=value, context=new_context)


def main():
    template = json.load(sys.stdin)

    print 'digraph g {'
    print 'rankdir=LR;'

    for param in template['Parameters']:
        print '{param} [label="{param}",shape=oval];'.format(param=param)

    print

    for resource, details in template['Resources'].iteritems():
        print r'{resource} [label="{resource}\n{type}",shape=box];'.format(resource=resource, type=details['Type'])

    for resource, details in template['Resources'].iteritems():
        find_refs(resource_name=resource, resource_object=details, context=None)

    print '}'


if __name__=='__main__':
    main()
