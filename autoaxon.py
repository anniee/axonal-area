#Automated Axonal Area: by Anne Vetto
#A simple program for general quantification of axonal degeneration/atrophy, the purpose
#is for a cursoy, automated estimate of an "atrophy number" for impression on whether a
#crossectional image of mouse lumbar (L5) spinal cord root axons are atrophied or healthy.
#This program assumes images are taken at the same maginification with comparable contrast
#and lighting.

#take image of axon, make new empty image, normalize to black and white by setting threshold
#and selecting to insert either a black or white pixel into the empty image
# since axon will appear darker and be assigned to black, the black pixels will be quantified
# increased diameter and thickness of axon indicates lack of pathology, so the greater the
#amount of black pixels, the closer to healthy axon on the spectrum it is.
# thus, a superficial axonal health score can be assigned, based on how close it is to 0 (degenerated) or 100.
