import xmos_image_utils


def test_msb_to_lsb():
    # Transforming msb to lsb twice must return the same stuff
    expected = b'\x80\x01'
    actual = xmos_image_utils.msb_to_lsb(expected)
    # Make sure something happened
    assert expected != actual
    actual = xmos_image_utils.msb_to_lsb(actual)
    # Make sure we got back same stuff after 2:nd transformation
    assert expected == actual
