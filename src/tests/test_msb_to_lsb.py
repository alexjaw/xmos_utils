import xmos_image_utils


def test_msb_to_lsb(data=None):
    # Transforming msb to lsb twice must return the same stuff
    expected = b'\x80\x01'
    actual = xmos_image_utils.msb_to_lsb(xmos_image_utils.msb_to_lsb(expected))
    assert expected == actual
