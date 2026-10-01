if(CONFIG_SHIELD_TORABO_TSUKI_LP_LEFT OR CONFIG_SHIELD_TORABO_TSUKI_LP_RIGHT)
  zephyr_library()
  zephyr_include_directories(${APPLICATION_SOURCE_DIR}/include)
  zephyr_library_sources(src/board.c src/mini_trackpad_init_reg.c)
endif()

target_sources_ifdef(CONFIG_ZMK_USB_BOOTMAGIC app PRIVATE src/usb_bootmagic.c)

if(CONFIG_DT_HAS_ZMK_USB_BOOTMAGIC_ENABLED AND NOT CONFIG_ZMK_USB_BOOTMAGIC)
    message(WARNING "zmk,usb-bootmagic is in the devicetree, but CONFIG_ZMK_USB_BOOTMAGIC is disabled (CONFIG_USB_DEVICE_STACK is required)")
endif()
