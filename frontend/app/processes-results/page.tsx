"use client";
import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { DataTable } from "@/components/dataTable/dataTable";
import LoadableContainer from "@/components/loadableContainer";
import { Process } from "@/lib/types";
import { columns } from "./columns";

export default function ProcessesResultsPage() {
  const searchParams = useSearchParams();
  const [processes, setProcesses] = useState<Process[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function fetchProcesses() {
      setIsLoading(true);
      try {
        const response = await fetch(
          `http://127.0.0.1:8000/api/processes/?${searchParams?.toString()}`
        );
        const data = await response.json();
        setProcesses(data.results);
      } catch (error) {
        console.error("Error fetching processes:", error);
      } finally {
        setIsLoading(false);
      }
    }
    fetchProcesses();
  }, [searchParams]);

  const filters = [
    { columnKey: "documentType", title: "Typ dokumentu" },
    { columnKey: "processStartDate", title: "Data rozpoczęcia" },
    { columnKey: "length_tag", title: "Długość" },
  ];

  return (
    <LoadableContainer>
      {isLoading ? (
        <div>Ładowanie...</div>
      ) : (
        <DataTable columns={columns} data={processes} filters={filters} />
      )}
    </LoadableContainer>
  );
}