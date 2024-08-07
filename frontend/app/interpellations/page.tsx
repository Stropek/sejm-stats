"use client";
import { DataTable } from "@/components/dataTable/dataTable";
import { columns, getColumnsWithClickHandler } from "./columns";
import LoadableContainer from "@/components/loadableContainer";
import { useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";
import { APIResponse, Interpellation } from "@/lib/types";
import { useFetchData } from "@/lib/api";
import { SkeletonComponent } from "@/components/ui/skeleton-page";

async function InterpellationsTable() {
  const searchParams = useSearchParams();
  const { data, isLoading, error } = useFetchData<APIResponse<Interpellation>>(
    `/interpellations/?${searchParams?.toString()}`
  );
  if (isLoading) return <SkeletonComponent />;
  if (error) return <>{error.message}</>;
  if (!data) return null;

  const filters = [
    { columnKey: "member", title: "Autor" },
    { columnKey: "sentDate", title: "Data wysłania" },
  ];
  return (
    <>
      <DataTable
        columns={getColumnsWithClickHandler()}
        data={data.results}
        filters={filters}
      />
    </>
  );
}

export default function InterpellationsPage() {
  return (
    <div className="mx-1">
      <Suspense fallback={<SkeletonComponent />}>
        <InterpellationsTable />
      </Suspense>
    </div>
  );
}
