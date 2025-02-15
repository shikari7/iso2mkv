#!/usr/bin/perl -w

# convert any ISO/iso in SOURCE to mkv in TARGET

# Eric D. Hendrickson
# ericdavidhendrickson@gmail.com
# Sat Jan  4 21:10:14 CST 2025

# To Do:

use strict;
use Getopt::Long;

(my $prog = $0) =~ s,.*/,,;

my $usage = "usage: $prog [--debug] [--help] [--file filename] [--target filename]\n";

# configurable options
my ($debug, $help, $list, $target);
GetOptions("debug" => \$debug,
	   "help" => \$help,
	   "file=s" => \$list,
	   "target=s" => \$target
	  ) or die $usage;

die $usage if $help;

# globals
my @files;
my $string = "";

$list ||= "/usr/local/lib/FILES_TO_ARCHIVE";
$target ||= "/export/archive.tgz";

# generate list of files to archive
open LIST, $list or exit;
while (<LIST>) {
  chomp;
  push @files, $_;
}
close LIST;

# 
foreach my $f (@files) {
  $string .= " \'$f\'";
}

system "tar czf $target$string";
