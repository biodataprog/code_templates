#!/usr/bin/env python3

# input MCL output file
orthomclfile = "Dothideomycetes.I15.mcl.out"

species_names = {}
orthologs = []
with open(orthomclfile,"r") as fh:
    for line in fh: # process each line in the file
        line = line.strip() # remove trailing newline
        row = line.split("\t")
        species_count = {}
        for gene in row:
            gene_id_split = gene.split("|")
            species = gene_id_split[0]
            # keep track of all the species seens so we know at end
            species_names[species] = 1
            if species in species_count:
                species_count[species] += 1
            else:
                species_count[species] = 1
                
        orthologs.append( species_count )

header = ["ORTHOLOG_GROUP"]
header.append(species_names.keys())
print("\t".join(map(str,header)))

orthonumber = 1
for ortholog in orthologs:
    final = ["ORTHO_%d"%(orthonumber)]    
    for species in species_names:
        if species in ortholog:
            final.append(ortholog[species])
        else:
            final.append(0)
    print("\t".join(map(str,final)))
    orthonumber += 1
