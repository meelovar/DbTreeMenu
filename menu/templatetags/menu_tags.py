import re

from django import template
from django.urls import reverse

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request_path = context["request"].path
    menu_items = MenuItem.objects.filter(menu__name=menu_name).order_by('parent_id')
    menu_nodes_map = {item.id: create_new_node(item) for item in menu_items}
    menu_tree = []
    selected_item = None

    for item in menu_nodes_map.values():
        parent_id = item["parent"]

        if parent_id is None:
            menu_tree.append(item)

            # Элементы первого уровня всегда показаны
            item["active"] = True
        else:
            parent_node = menu_nodes_map[parent_id]

            parent_node["children"].append(item)

        if item["path"] == request_path:
            selected_item = item

    if selected_item:
        selected_item["active"] = True
        selected_item["selected"] = True

        # Показать показать первый уровень дочерних элементов
        # под выбранным
        for child in selected_item["children"]:
            child["active"] = True

        parent_id = selected_item["parent"]

        # Показать все родительские элементы выше выбранного
        while parent_id is not None:
            prev_node = menu_nodes_map[parent_id]

            prev_node["active"] = True
            parent_id = prev_node["parent"]

    return {"menu_name": menu_name, "menu_items": menu_tree}


def create_new_node(menu_item):
    item_path = menu_item.path
    url_path_match = re.match(r"^/.*$", item_path)

    if not url_path_match:
        item_path = reverse(item_path)

    result = {
        "id": menu_item.id,
        "name": menu_item.name,
        "parent": menu_item.parent_id,
        "path": item_path,
        "active": False,
        "selected": False,
        "children": [],
    }

    return result
