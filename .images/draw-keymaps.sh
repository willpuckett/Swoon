keymap="zmk-config/boards/shields/swoon/swoon.keymap"
LAYOUTS=('NC' 'QWERTY' 'ENGRAM' 'ENGRAMMER')

for l in {1..3}; do
    echo "Rendering Layout ${LAYOUTS[l]}"
    yml=".images/swoon${l}.yml"
    KEYMAP_zmk_preamble="#define LAYOUT ${l}" keymap parse -c 10 -z ${keymap} > "${yml}" && \
    keymap draw -k ferris/sweep "${yml}" > ".images/swoon_${LAYOUTS[l]}.svg"
    [[ $? -ne 0 ]]  && exit 1
    rm "${yml}"
done
