def can_move_ne(my_bw, my_charge, peer1_bw, peer1_charge, peer2_bw, peer2_charge):
    """
    my_bw: bandwidth of My_NE (6Go)
    my_charge: percentage (60%)
    peerX_bw: current bandwidth (20Go)
    peerX_charge: current load

    We add my_bw/2 to Peer1 and Peer2.
    We add my_charge/2 to Peer1 and Peer2.
    """

    # 100% --- 6Go
    # 60% --- x Go
    # load to moving (Go)
    move_load = (my_charge * my_bw) / 100
    half_move_load = move_load / 2
    
    
    # Distribute load equally
    # 100% --- 20Go
    # y % --- half_move_load Go
    peer1_new_charge = peer1_charge + ((half_move_load * 100) / peer1_bw)
    peer2_new_charge = peer2_charge + ((half_move_load * 100) / peer2_bw)
    
    # peer2_new_charge = peer2_charge + (half_move_load / 2)

    # Threshold = 60%
    limit = 60

    return {
        "peer1_new": round(peer1_new_charge, 2),
        "peer2_new": round(peer2_new_charge, 2),
        "peer1_ok": peer1_new_charge <= limit,
        "peer2_ok": peer2_new_charge <= limit,
        "can_move": (peer1_new_charge <= limit and peer2_new_charge <= limit)
    }
