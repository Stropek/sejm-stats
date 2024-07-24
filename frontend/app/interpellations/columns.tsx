"use client";

import { DataTableColumnHeader } from "@/components/columns";
import { Interpellation } from "@/lib/api";
import { ColumnDef } from "@tanstack/react-table";

export const columns: ColumnDef<Interpellation>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="ID" />
    ),
  },
  {
    accessorKey: "title",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Tytuł" />
    ),
  },
  {
    accessorKey: "member",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Autor" />
    ),
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
  {
    accessorKey: "sentDate",
    header: ({ column }) => (
      <DataTableColumnHeader column={column} title="Data wysłania" />
    ),
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id));
    },
  },
];