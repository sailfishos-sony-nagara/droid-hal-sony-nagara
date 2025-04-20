%define device pdx223

%define lunch_device aosp_xqct54-ap2a-user; cd kernel/sony/msm-5.15/common-kernel; ./build-kernels-clang.sh -d %{device} -O ../../../../out/target/product/%{device}/obj/kernel; cp dtbo-%{device}.img ../../../../out/target/product/%{device}/dtbo.img; cd -

%include rpm/droid-hal-common.inc
%include dhd/droid-hal-device.inc
