def stock_alert(
    inventory_level,
    reorder_point
):

    if inventory_level < reorder_point:
        return "Reorder Needed"

    return "Sufficient Stock"