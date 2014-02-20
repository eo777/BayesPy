#!/usr/bin/python
#
# A library for finding a dirichlet mixture mixture from count data
# By: Max Sklar
# @maxsklar
# https://github.com/maxsklar

################################################
############ UNFINISHED
#################################################

# Copyright 2013 Max Sklar

import math
import random
import logging
import dirichletMultinomialEstimation as DME

class DirichletMixtureModel:
  # C: number of components
  # K: number of categories
  # dirichlets: a list of C dirichlet distributions, each with K parameters
  # mixture: a C-dimensional multinomial describing the mixture probabilities of the C dirichlets.
  def __init__(self, C, K, dirichlets, mixture):
      self.C = C
      self.K = K
      
      if (len(dirichlets) != C):
        logging.error("dirichlets param must have C=" + str(C) + " components")
      
      for d in dirichlets:
        if (len(d) != K): logging.error("dirichlet distributions must have K=" + str(K) + " parameters")
        
      if (len(mixture) != C): logging.error("mixture probabilities must have C=" + str(C) + " components")
      
      self.dirichlets = dirichlets
      self.mixture = mixture
      
class DirichletMixtureModelHyperparams:
  # C: number of components
  # K: number of categories
  # beta, W: the hyperdirichlet over the dirichlet distribution
  # mixtureDirich: a dirichlet distribution representing the prior over the mixture parameters
  def __init__(self, C, K, beta, W, mixtureDirich):
    self.C = C
    self.K = K
    
    if (len(beta) != K): logging.error("hyperdirichlet beta have K=" + str(K) + " parameters")
    self.beta = beta
    self.W = W
    
    if (len(mixtureDirich) != C): logging.error("mixture dirichlet must have C=" + str(C) + " components")
    self.mixtureDirich = mixtureDirich