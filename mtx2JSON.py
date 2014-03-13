import numpy as np
import scipy.io as sio
import networkx as nx
import optparse

modes = ['graph','pathway']

def write_json(G):
    from networkx.readwrite import json_graph
    return str(json_graph.dumps(G))
    
def tprob_to_json(tprob,c):
    tprob = tprob.multiply(tprob > c)
    G = nx.from_numpy_matrix(tprob.todense())
    return write_json(G)
    
def tp_to_json(tprob,n,sources,sinks):
    from msmbuilder import tpt
    paths = tpt.find_top_paths(sources,sinks,tprob=tprob,num_paths=n)
    G = nx.DiGraph()
    for j,i in enumerate(paths[0][::-1]):
        G.add_node(str(i[0]),type="source")
        for k in range(1,len(i)):
            G.add_node(str(i[k]),type="none")
            G.add_edge(str(i[k-1]),str(i[k]),weight=paths[2][::-1][j])
        G.add_node(str(i[-1]),type="sink")
    return write_json(G)
    
def parse_cmdln():
    import os
    parser=optparse.OptionParser()
    parser.add_option('-m','--mode',dest='m',type='string',default='graph')
    parser.add_option('-t','--transition_matrix',dest='t',type='string')
    parser.add_option('-c','--cut_off',dest='c',type='float',default=0.0)
    parser.add_option('-n','--n_paths',dest='n',type='int',default=5)
    parser.add_option('-s','--sources',dest='sources',type='string')
    parser.add_option('-e','--sinks',dest='sinks',type='string')
    (options, args) = parser.parse_args()
    if options.m not in modes:
        parser.error('Given mode is not recognized')
    if not options.t:
        parser.error('You need to at least supply a transition matrix.')
    if options.m is 'pathway':
        if not options.sources and not options.sinks:
            parser.error('You need to input both sources AND sinks')
    return (options, args)
    
if __name__=="__main__":
    (options,args) = parse_cmdln()
    tprob = sio.mmread(options.t)
    if options.m is 'graph':
        print tprob_to_json(tprob,options.c)
    else:
        sources=np.loadtxt(options.sources,dtype=int)
        sinks=np.loadtxt(options.sinks,dtype=int)
        print tp_to_json(tprob,options.n,sources,sinks)
