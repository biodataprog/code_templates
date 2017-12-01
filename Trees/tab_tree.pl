#!/usr/bin/perl
use Bio::TreeIO;

my $in = Bio::TreeIO->new(-format => 'newick', -fh => \*DATA);
my $out = Bio::TreeIO->new(-format => 'tabtree');
while(my $t = $in->next_tree ){
  $out->write_tree($t);
print "\n";
}		 

__DATA__
(A,(B,C));
((A,B),(C,D));
(A,(B,(C,D)))
