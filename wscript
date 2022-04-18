#! /usr/bin/env python
# encoding: utf-8
# mittorn, 2018

from waflib import Logs
import os

VERSION = '1.A.XX'
APPNAME = 'relcc'
top = '.'

def options(opt):
	opt.load('compiler_cxx clang_compilation_database')
	pass

def configure(conf):
	conf.load('compiler_cxx')
	pass

def build(bld):
	libs = [ 'M' ]

	source = bld.path.ant_glob(['src/**/*.c'])

	includes = [ 'src/' ]

	bld.shlib(
		source   = source,
		target   = 'relcc',
		features = 'cxx',
		includes = includes,
		use      = libs,
		rpath    = '.'
	)
