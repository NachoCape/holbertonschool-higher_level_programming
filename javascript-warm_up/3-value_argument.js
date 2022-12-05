#!/usr/bin/node

import { argv } from 'process';

if (argv[2]) { console.log(argv[2]); } else { console.log('No argument'); }
